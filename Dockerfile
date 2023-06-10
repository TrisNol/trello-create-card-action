FROM python:3.9.10-slim-buster
WORKDIR /github/workspace

COPY . /github/workspace/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python", "main.py"]