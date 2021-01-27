FROM python:3.9-slim

RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

COPY ./changelog_generator.py /changelog_generator.py

CMD [ "python", "/changelog_generator.py" ]