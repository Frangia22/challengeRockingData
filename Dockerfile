FROM python:alpine3.19

WORKDIR /app

COPY . /app

CMD ["python", "app.py"]