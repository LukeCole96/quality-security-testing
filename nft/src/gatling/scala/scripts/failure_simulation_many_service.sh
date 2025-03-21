#!/bin/bash

app_containers=("juice-shop-1" "juice-shop-2" "juice-shop-3")

selected_containers=($(shuf -e "${app_containers[@]}" -n 2))

echo "Permanently taking down: ${selected_containers[*]}"
docker-compose stop "${selected_containers[@]}"
