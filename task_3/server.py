from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

@app.route('/ping', methods=['POST'])
def ping():
    return jsonify({
        'type': 'pong',
        'time': datetime.now().isoformat()
    })

@app.route('/data', methods=['POST'])
def data():
    data = request.json
    response = {
        'jsonrpc': data.get('jsonrpc'),
        'method': data.get('method'),
        'time': datetime.now().isoformat()
    }
    return jsonify(response)

app.run(host='0.0.0.0', port='5000')
