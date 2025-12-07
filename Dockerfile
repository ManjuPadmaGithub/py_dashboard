# Use an official Python runtime as a base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit's default port
EXPOSE 8501

# Run Streamlit app when container starts
CMD ["streamlit", "run", "my_app/main.py", "--server.port=8501", "--server.address=0.0.0.0"]