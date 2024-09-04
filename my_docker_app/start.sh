#!/bin/bash

echo "################################"
echo "# Hello from docker container! #"
echo "################################"
echo " Hi "
while true; do

	current_time=$(date +"%T")
	sleep 1
	echo "Current time from container: $current_time"

done
