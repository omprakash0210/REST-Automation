
FROM nginx:latest

COPY ./app /app

RUN apt-get update

RUN apt-get install -y python2.7 python-pip

RUN pip install -r /app/requirements.txt

CMD ["python", "/app/main.py"]
