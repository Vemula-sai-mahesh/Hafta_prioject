# FROM ubuntu:20.04 as ubuntu-hafta-1
# RUN apt-get update && apt-get install -y libcurl4-openssl-dev

#Docker file seems operational 
# FROM hafta-1:ubuntu as dev-envs
FROM python:3.10.12-alpine3.18 as python-hafta-1
# RUN apt-get update && apt-get install -y libcurl4-openssl-dev

WORKDIR /app
COPY . /app

RUN apk --no-cache add libcurl

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt
# RUN apt-get update && apt-get install -y 

CMD [ "python3", "run.py" ]
EXPOSE 8000

VOLUME /tmp
# CMD ["python3", "run.py"]