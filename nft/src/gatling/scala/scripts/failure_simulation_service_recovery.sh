#!/bin/bash

app_containers=("juice-shop-1" "juice-shop-2" "juice-shop-3")

random_container=${app_containers[$RANDOM % ${#app_containers[@]}]}

echo "Taking down $random_container"
docker-compose stop $random_container

sleep_time=$(( (RANDOM % 3) + 10 ))
echo "Sleeping for $sleep_time seconds"
sleep $sleep_time

echo "Bringing up $random_container"
docker-compose start $random_container