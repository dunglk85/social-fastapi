FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .
COPY requirements-dev.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir -r requirements-dev.txt
# Copy the application code
COPY . .

# Expose the port FastAPI runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]