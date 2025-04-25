# Dockerfile
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY wait-for.sh /app/wait-for.sh
RUN chmod +x /app/wait-for.sh

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY project /app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
