# FROM ubuntu:20.04 as ubuntu-hafta-1
# RUN apt-get update && apt-get install -y libcurl4-openssl-dev

#Docker file seems operational 
# FROM hafta-1:ubuntu as dev-envs
FROM --platform=$BUILDPLATFORM python:3.10.12-alpine3.18 as python-hafta-1
# RUN apt-get update && apt-get install -y libcurl4-openssl-dev

WORKDIR /app
COPY requirements.txt /app

# RUN apk --no-cache add libcurl

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt
# RUN apt-get update && apt-get install -y 

COPY . .

ENV FLASK_ENV development
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0


EXPOSE 8000


VOLUME /tmp



RUN apk update && apk add --no-cache
# install Docker tools (cli, buildx, compose)
RUN addgroup -S docker && \
    adduser -S --shell /bin/bash --ingroup docker vscode
COPY --from=gloursdocker/docker / /

CMD ["python3", "run.py"]