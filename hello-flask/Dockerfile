FROM python:3.6.1-slim

USER root

WORKDIR /root

RUN pip install Flask

EXPOSE 5000

COPY server.py server.py

CMD ["python", "server.py"]
