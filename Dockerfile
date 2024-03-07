# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt || exit 1

# Expose the port 8501
EXPOSE 8501

# Health Check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Define the command to run the application when the container starts
ENTRYPOINT ["streamlit", "run", "1_🙂Homepage.py", "--server.port=8501", "--server.address=0.0.0.0"]
