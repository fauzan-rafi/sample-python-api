FROM python:3.10-rc-alpine

RUN pip install flask

COPY main.py /opt/

ENTRYPOINT FLASK_APP=/opt/main.py flask run --host=0.0.0.0 --port=80
