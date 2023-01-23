FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./app /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt

ENV PORT=8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
