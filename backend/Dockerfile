FROM python:3.6.4@sha256:bf0718e2882cabc144c9c07d758b09c65efc104a6ddc72a9a976f8b26f67c2ee

RUN pip install pipenv

# -- Install Application into container:
RUN set -ex && mkdir /app

WORKDIR /app

# -- Adding Pipfiles
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --deploy --system

# -- Install dependencies:
COPY . /app/

# # uWSGI will listen on this port
EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=pycon_ml.settings.prod

# # uWSGI configuration (customize as needed):
ENV UWSGI_WSGI_FILE=pycon_ml/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=3
ENV UWSGI_THREADS=10 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# # Start uWSGI
CMD ["uwsgi", "--http-auto-chunked", "--http-keepalive", "--static-map", "/static=/app/static"]
