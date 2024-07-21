# syntax=docker/dockerfile:1 
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy files
COPY . /app

# Install dependencies
RUN pip3 install -r requirements.txt

# Run the application
EXPOSE 5000
CMD python3 ./app.py
