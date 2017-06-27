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
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify(message='hello world')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

### Test your application
``` sh
python server.py
```

### Test with Docker
``` sh
docker build -t TAG .
docker images
docker create -p HPORT:CPORT --name CONTAINER TAG
docker start CONTAINER
docker ps
curl localhost:HPORT
docker stop CONTAINER
```

### Deploy on Bluemix
``` sh
bx login
bx ic init
bx ic build -t TAG .
bx ic images
bx ic namespace-get
bx ic create -p HPORT:CPORT --name CONTAINER NAMESPACE/TAG
bx ic ip-request
bx ic ips
bx ic ip-bind IP CONTAINER
bx ic start CONTAINER
curl IP:HPORT
```

[docker]: https://www.docker.com/
[bx-cli]: https://console.bluemix.net/docs/cli/reference/bluemix_cli/index.html#getting-started
[bx-ic]: https://console.bluemix.net/docs/containers/container_cli_cfic_install.html#install_plugin