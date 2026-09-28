#!/bin/bash
# scripts/deploy.sh

echo "Deploying Open Source Project Wiki..."

# Variables
CONTAINER_NAME="project-wiki"
IMAGE_NAME="project-wiki-image"
PORT=80

# Build Docker image
echo "Building Docker image..."
docker build -t $IMAGE_NAME .

# Stop existing container if running
if [ $(docker ps -q -f name=$CONTAINER_NAME) ]; then
    echo "Stopping existing container..."
    docker stop $CONTAINER_NAME
fi

# Remove existing container if it exists
if [ $(docker ps -aq -f status=exited -f name=$CONTAINER_NAME) ]; then
    echo "Removing existing container..."
    docker rm $CONTAINER_NAME
fi

# Run new container
echo "Running new container..."
docker run -d --name $CONTAINER_NAME -p $PORT:80 $IMAGE_NAME

echo "Deployment complete! Application is running on port $PORT."
