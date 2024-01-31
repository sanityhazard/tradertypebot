FROM python:3.10

# Path: /app
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
  
COPY . .

EXPOSE 80

CMD ["python", "main.py"]
