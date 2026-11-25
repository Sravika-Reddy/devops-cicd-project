
# Use Python as the base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose application port
EXPOSE 5000

# Start Flask application
CMD ["python", "app.py"]
