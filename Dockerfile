FROM python:3.9.2-alpine3.13

WORKDIR /app

RUN apk add --no-cache bash

COPY . . 

RUN chmod +x run

ENTRYPOINT ["./run"]
