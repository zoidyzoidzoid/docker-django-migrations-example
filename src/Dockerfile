FROM python:3

RUN apt-get update && apt-get install -y \
        nginx supervisor --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* && \
    service nginx stop && \
    service supervisor stop

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

VOLUME ~/.cache

RUN pip install -U pip setuptools virtualenv wheel

COPY requirements.txt /usr/src/app/

RUN pip install -r requirements.txt

COPY . /usr/src/app
COPY nginx.conf /etc/nginx/
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80
CMD ["supervisord"]
