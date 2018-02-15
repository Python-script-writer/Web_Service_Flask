FROM python:3.5.3
ADD . /todo
WORKDIR /todo

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY app app
COPY run.py config.py

ENV FLASK_APP run.py

EXPOSE 5000
