FROM python:3.9

RUN pip install fastapi
RUN pip install "uvicorn[standard]"

WORKDIR /app
COPY . .

EXPOSE 80

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
