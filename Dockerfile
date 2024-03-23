
FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

RUN /bin/sh -c '/app/docker-entrypoint.sh'

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
