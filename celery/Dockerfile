FROM python:3-alpine
ENV PYTHONUNBUFFERED 1

# base
RUN apk add --update git
# postgres
RUN apk add --update postgresql-dev gcc python3-dev musl-dev
# pillow
RUN apk add --update jpeg-dev zlib-dev

RUN git clone https://github.com/UrLab/DocHub.git /code
WORKDIR /code

COPY local.py /code/www/config/

RUN pip install -r requirements.txt

HEALTHCHECK CMD ["celery", "-A", "www", "inspect", "ping"]
CMD ["celery", "-A", "www", "worker", "-l", "info"]
