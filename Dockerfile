# Use an official Python base image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy all project files into the container
COPY . /app

# Install dependencies
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Expose port (Flask default is 5000)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
