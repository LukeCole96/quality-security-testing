#!/bin/bash

app_containers=("juice-shop-1" "juice-shop-2" "juice-shop-3")

for container in "${app_containers[@]}"; do
  echo "Rolling out new version for: $container"

  echo "Stopping $container"
  docker-compose stop "$container"

  echo "Recreating and starting $container with latest version"
  docker-compose up -d --no-deps --force-recreate "$container"

  echo "Waiting for $container to be healthy..."
  sleep 10

  echo "$container updated successfully."
  echo "------------------------------------------"
done
