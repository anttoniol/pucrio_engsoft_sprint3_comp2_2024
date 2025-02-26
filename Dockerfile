FROM python:3.10

# The EXPOSE instruction indicates the ports on which a container
# will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
EXPOSE 5000

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this instruction
# creates a directory with this name if it doesn’t exist
WORKDIR /app

COPY . /app

ENV PYTHONPATH /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


# Run app when the container launches
CMD python3 /app/api/controller.py
