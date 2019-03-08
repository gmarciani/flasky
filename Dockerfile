# Flasky / Latency
#
# VENDOR                Giacomo Marciani
# VERSION               1.0.0

FROM python:3.6

LABEL Description="Flasky / Latency" Vendor="Giacomo Marciani" Version="1.0.0"

# ARGUMENTS
ARG rootdir=.

# OS UPDATE
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev

# SOURCES
ADD $rootdir /app/flasky

# Change working directory
WORKDIR /app/flasky

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["python3", "app.py"]