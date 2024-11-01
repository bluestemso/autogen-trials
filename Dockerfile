# Base image with Python
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your code
COPY . .

# Command to run your code
CMD ["python", "main.py"] 