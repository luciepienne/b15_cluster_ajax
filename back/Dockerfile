FROM python:3.11-alpine

# Install system dependencies new code due to issues with dependencies with numpy
RUN apk add --no-cache gcc musl-dev

# Set working directory
WORKDIR /app

# Copy your application code
COPY . .

# Copy requirements file and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8000

# Command to run the application
CMD ["python", "api_models.py"]
