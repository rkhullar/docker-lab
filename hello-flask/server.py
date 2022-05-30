import json
import os
from pathlib import Path

from flask import Flask, jsonify

app = Flask(__name__)
service_name = os.getenv('SERVICE_NAME', 'hello-flask')
service_port = int(os.getenv('SERVICE_PORT', '8000'))

with Path('secrets.json').open('r') as f:
    extra_data = json.load(f)


@app.route('/')
def index():
    return jsonify(
        service_name=service_name,
        service_port=service_port,
        message='hello world',
        extra=extra_data
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=service_port)
