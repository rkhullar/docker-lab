FROM python:3.6.1-slim

RUN apt-get update && apt-get install -y nano curl build-essential graphviz python3-dev

COPY requirements.txt .
COPY pip-install .
RUN ./pip-install

# EXPOSE 4000-4002 5000 8786-8788 9786 
EXPOSE 5000 8787 8888
