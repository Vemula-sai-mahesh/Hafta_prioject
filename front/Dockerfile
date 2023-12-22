FROM node:16.20.2

WORKDIR /front
COPY . .

RUN npm install

EXPOSE 3000

ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000

ENTRYPOINT ["front1" ]

