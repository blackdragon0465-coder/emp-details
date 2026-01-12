FROM python:3.13-slim

WORKDIR /app

COPY emp_details.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "emp_details.py", "101", "Pothyshwer", "28"]
