# Ligth weight Python image as the base image
FROM python:3.8-slim-buster

# Set the working directory
WORKDIR /app

# Copy the Python script and requirements file to the container
COPY app.py /app/
COPY requirements.txt /app/
COPY .env /app/.env

# create a virtual environment
RUN python3 -m venv venv

# Activate the environment
RUN . ./venv/bin/activate


# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install python-dotenv


# Expose the port that the Flask app will run on
EXPOSE 5000

# Define the command to run your Flask app
CMD [ "python", "app.py"]

