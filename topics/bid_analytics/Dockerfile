FROM python:3.9-slim

WORKDIR /topics

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "analytics.py"]

