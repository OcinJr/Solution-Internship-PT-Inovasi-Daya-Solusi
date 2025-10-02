#!/bin/bash

# initialize variables to store image and container name
IMAGE_NAME="intern1-container1"
CONTAINER_NAME="container1"

# stop and remove the old container if it exists
echo "Stopping and removing old container..."
docker stop $CONTAINER_NAME || true
docker rm $CONTAINER_NAME || true

# build the new Docker image
echo "Building Docker image: $IMAGE_NAME..."
docker build -t $IMAGE_NAME .

# run the new container from the image
echo "Running new container: $CONTAINER_NAME..."
docker run --name $CONTAINER_NAME $IMAGE_NAME

echo "finished...."