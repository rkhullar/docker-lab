ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-alpine
USER root
WORKDIR /root
RUN apk install --no-cache jq && pip install flask
COPY server.py server.py
RUN --mount=type=secret,id=a --mount=type=secret,id=b \
    ./install-secrets.sh && rm install-secrets.sh
CMD ["python", "server.py"]
