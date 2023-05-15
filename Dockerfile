FROM python:3.9-slim

COPY ./app /app
COPY requirements.txt /app/requirements.txt
COPY packages.txt /app/packages.txt

WORKDIR /app

# RUN mkdir predictedSamples

RUN apt-get update && \
    if [ $DEV = "true" ]; \
        then xargs -a packages.txt apt-get install -y  \
        build-essential \
        curl \
        software-properties-common ; \
    fi && \ 
    rm -rf /var/lib/apt/lists/* && \
    pip install --upgrade pip

 
RUN pip3 install -r requirements.txt && \
    rm -rf /app/requirements.txt /app/packages.txt

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health


