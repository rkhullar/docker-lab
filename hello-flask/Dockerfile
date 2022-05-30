ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-alpine
USER root
WORKDIR /root
RUN apk add --no-cache jq && pip install flask
COPY install-secrets.sh server.py ./
RUN --mount=type=secret,id=a --mount=type=secret,id=b \
    ./install-secrets.sh && rm install-secrets.sh
CMD ["python", "server.py"]
