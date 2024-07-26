#!/bin/bash

# Define an array of service directories
services=("queues" "rest" "topics")

# Loop through each service directory and run docker-compose up
for service in "${services[@]}"; do
    echo "Starting services in $service..."
    (cd "$service" && docker-compose up -d)
    if [ $? -eq 0 ]; then
        echo "Successfully started services in $service"
    else
        echo "Failed to start services in $service"
    fi
done

echo "All services have been started."
