FROM python:3.9.10-slim-buster

COPY . /app

RUN pip3 install -r /app/requirements.txt

ENTRYPOINT ["python", "/app/main.py"]