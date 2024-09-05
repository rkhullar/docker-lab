FROM python:3.12-alpine
ARG USER='app'
RUN adduser --system --shell /bin/sh --home /app ${USER}

USER ${USER}
WORKDIR /app

RUN pip install flask
COPY --chown=${USER} server.py .
CMD ["python", "server.py"]
