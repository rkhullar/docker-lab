## Bluemix Adventures - Part 1
Rajan Khullar

### Objective
Create and deploy a hello world Flask application as a Docker image on Bluemix.

### Prerequisistes
1. [Docker][docker]
2. [Bluemix CLI][bx-cli]
3. [Container Plugin][bx-ic]

### Write the application
``` sh
mkdir path/to/project
cd path/to/project
touch Dockerfile requirements.txt server.py
```
```sh
# Dockerfile
FROM python:3.6.1-slim
WORKDIR /app
ADD . /app
RUN pip install -r requirements.txt
EXPOSE 5000
ENV NAME World
CMD ["python", "server.py"]
```
```sh
# requirements.txt
Flask
```
``` python
# server.py
from flask import Flask, jsonify
import os

app = Flask(__name__)

name = os.getenv('NAME')

@app.route('/')
def index():
    return jsonify(message=f'Hello {name}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Test your application
``` sh
python server.py
```

### Test with Docker
``` sh
# build an image from the docker file
docker build -t TAG .
# list images
docker images
# create a container with mapped ports
docker create -p HPORT:CPORT --name CONTAINER TAG
# start the container
docker start CONTAINER
# list running containers
docker ps
# test the container works
curl localhost:HPORT
# stop the container
docker stop CONTAINER
```

### Deploy on Bluemix
``` sh
# login to bluemix console
bx login
# initialize registry
bx ic init
# build and push image 
bx ic build -t TAG .
# list available images
bx ic images
# show repository name
bx ic namespace-get
# create container
bx ic create -p HPORT:CPORT --name CONTAINER NAMESPACE/TAG
# request an ip address
bx ic ip-request
# list ip addresses
bx ic ips
# bind ip to container
bx ic ip-bind IP CONTAINER
# start the container
bx ic start CONTAINER
# test the container
curl IP:HPORT
```

[docker]: www.docker.com/
[bx-cli]: clis.ng.bluemix.net/ui/home.html
[bx-ic]: console.bluemix.net/docs/containers/container_cli_cfic_install.html#install_plugin