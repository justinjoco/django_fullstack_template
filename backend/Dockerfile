FROM python:3.12-alpine

RUN mkdir -p /home/app
WORKDIR /home/app
COPY . /home/app

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "./docker-entrypoint.sh" ]