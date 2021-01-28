import re
import shlex
import subprocess
import time
import datetime

def get_commit_log():
    output = subprocess.check_output(shlex.split('git log --pretty=%s --color'),
stderr=subprocess.STDOUT)
    output = output.decode('ascii')
    output = output.split('\n')
    return output

def strip_commits(commits):
    # Get the following prefixes from Conventional Commit Specification:
    # fix, feat, ci, refactor, perf, test
    output = []
    for line in commits:
        if re.findall(r'^(fix|feat|ci|refactor|perf|test)', line):
            output.append(line)
    return output

def overwrite_changelog(commits):
    print ("Writing the following commits:\n{}".format(commits))
    with open("/github/home/CHANGELOG.md", "w+") as file:
        file.write('# Changelog %s \n\n## Features\n\n') % (datetime.datetime.now().ctime())
        for feat in commits:
            if re.findall(r'^feat', feat):
                file.write('* {}\n'.format(feat))
        file.write("\n## Bug Fixes\n\n")
        for fix in commits:
            if re.findall(r'^fix', fix):
                file.write('* {}\n'.format(fix))
        file.write("\n## Performance Improvements\n\n")
        for perf in commits:
            if re.findall(r'^perf', perf):
                file.write('* {}\n'.format(perf))
        file.write("\n## Other\n\n")
        for other in commits:
            if re.findall(r'^(refactor|test|ci)', other):
                file.write('* {}\n'.format(other))
        file.write('\n\n > Changelog automatically generated via GitHub Actions')
        file.close()
    return

def main():
    commits = get_commit_log()
    commits = strip_commits(sorted(commits))
    overwrite_changelog(commits)

main()
