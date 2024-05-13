from flask import Flask, jsonify, request
import socket

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_hostname():
    hostname = socket.gethostname()
    endpoint = request.endpoint
    return jsonify({"hostname": hostname, "endpoint": endpoint, "branch": "dev"})

if __name__ == '__main__':
    app.run(debug=True)
