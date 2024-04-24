FROM python:3.11-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the local directory's contents into the container at /app
COPY . .

# Install dependencies from requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that the Flask application runs on
EXPOSE 5000

# Command to run the Flask application
CMD ["python", "app.py"]
