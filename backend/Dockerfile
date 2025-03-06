# Use official Python image
FROM python:3.12

# Set the working directory
WORKDIR .

# Copy only requirements first (for better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the actual FastAPI project files
COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/"

# Expose port 8000 for FastAPI
EXPOSE 8000

# Ensure the script is executed within the container
ENTRYPOINT ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
