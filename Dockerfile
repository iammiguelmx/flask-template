FROM alpine:latest

LABEL maintainer "prueba@gmail.com"

RUN apk add cmd:pip3 --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]