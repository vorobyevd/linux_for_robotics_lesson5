#!/bin/python3

import datetime
import time
import os
name = os.environ['SERVICE_NAME']

if __name__ == "__main__":
	while True:
		now = datetime.datetime.now()
		print(f"Hello from service: {name}. current time is: {now.time()}")
		time.sleep(2)
