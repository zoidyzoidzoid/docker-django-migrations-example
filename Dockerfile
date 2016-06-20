FROM python:3

RUN apt-get update && apt-get install -y \
        nginx supervisor --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* && \
    service nginx stop && \
    service supervisor stop

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

RUN pip install --no-cache-dir -U pip setuptools virtualenv wheel

COPY src/requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt
COPY src /usr/src/app

COPY configs/nginx.conf /etc/nginx/
COPY configs/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80
CMD ["supervisord"]
