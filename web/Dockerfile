FROM python:3-alpine
ENV PYTHONUNBUFFERED 1

# base
RUN apk add --update git nodejs curl
# postgres
RUN apk add --update postgresql-dev gcc python3-dev musl-dev
# pillow
RUN apk add --update jpeg-dev zlib-dev

RUN git clone https://github.com/UrLab/DocHub.git /code
WORKDIR /code

COPY local.py /code/www/config/

RUN pip install -r requirements.txt

RUN npm install --no-progress
RUN npm run  build
RUN ./manage.py collectstatic --noinput -v 0

HEALTHCHECK CMD ["curl", "-f", "http://0.0.0.0:8000"]

EXPOSE 8000
CMD ["./manage.py", "runserver", "0.0.0.0:8000"]
