FROM trial7:latest

WORKDIR /hafta

COPY requirements.txt .

RUN mkdir front
COPY /front/package.json /front/

RUN cd front && npm install && cd .. && pip install -r requirements.txt

COPY . .



ENV NUXT_HOST=0.0.0.0
ENV NUXT_PORT=3000
ENV FLASK_HOST=0.0.0.0
ENV FLASK_PORT=5234

EXPOSE 3000
EXPOSE 5234

# WORKDIR /front
# CMD [ "npm","run","dev" ]







