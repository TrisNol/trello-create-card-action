FROM python:3.9.10-slim-buster
WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

ENTRYPOINT ["ls -l", "&&", "python", "main.py"]