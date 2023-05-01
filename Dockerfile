FROM python:3.9

WORKDIR /api

COPY ./requirements.txt /api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /api/requirements.txt

COPY ./app /api/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]