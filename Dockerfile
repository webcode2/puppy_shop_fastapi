FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    build-essential \
    --no-install-recommends \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /pupy_shop

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the FastAPI app and Alembic files into the container
COPY . .
COPY alembic.ini .

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Start the FastAPI application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

