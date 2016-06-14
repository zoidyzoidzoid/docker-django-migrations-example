import os

bind = "unix:/tmp/gunicorn.sock"
chdir = "/usr/src/app"
loglevel = "INFO"
workers = "3"
worker_connections = 1024

errorlog = "-"
accesslog = "-"

if os.environ.get('DJANGO_DEBUG', 'False').lower() == 'true':
    reload = True
