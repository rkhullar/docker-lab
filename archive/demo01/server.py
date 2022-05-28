from flask import Flask, jsonify
import os

app = Flask(__name__)

name = os.getenv('NAME')

@app.route('/')
def index():
    return jsonify(message=f'Hello {name}')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
