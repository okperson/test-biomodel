FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=main.py
ENV FLASK_ENV=development 

EXPOSE 5000

CMD [ "flask", "--app", "main.py", "run", "--host=0.0.0.0", "--port=5000", "--debug" ]