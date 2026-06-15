# Use the official Python 3.12 slim image
FROM python:3.12-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY ./app /app

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app.main:app"]
