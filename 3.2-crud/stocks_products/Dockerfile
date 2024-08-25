FROM python:3.12

WORKDIR /apps
ADD .env.docker /apps/.env

ENV APP_NAME=DOCKER_DEMO

COPY . /apps
RUN pip install -r /apps/requirements.txt

CMD ["gunicorn", "stocks_products.wsgi:application", "-b", "0.0.0.0:8000"]