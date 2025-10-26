# Use official Python runtime as base image
FROM python:latest

# Set working directory in container
WORKDIR /app

# Copy requirements.txt (if you have one)
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Install Flask
RUN pip install flask

# Copy the Flask application file
COPY flask_app.py .

# Expose port 5050
EXPOSE 5050

# Command to run the Flask application
CMD ["python", "-m", "flask_app", "run", "--host=0.0.0.0", "--port=5050"]