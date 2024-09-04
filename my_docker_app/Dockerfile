FROM ubuntu:24.04

RUN apt update &&\ 
    apt-get install -y python3\
    python3-pip\
    nano

   	
WORKDIR /app

COPY . /app

CMD pip install -r requirements.txt

ENTRYPOINT ["/bin/bash", "start.sh"]
