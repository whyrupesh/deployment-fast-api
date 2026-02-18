# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies (if any needed for psycopg2/asyncpg, though binary wheels usually suffice)
# RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# This layer is cached unless requirements.txt changes
# Install any needed packages specified in requirements.txt
# This layer is cached unless requirements.txt changes
RUN pip install --no-cache-dir -r requirements.txt

# Set Hugging Face cache directory
ENV HF_HOME=/app/cache/huggingface

# Pre-download the model to cache it in the image layer
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')"

# Copy the rest of the application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
