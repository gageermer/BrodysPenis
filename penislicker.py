from flask import Flask, request, jsonify
import requests
import json
import hashlib
import os
from datetime import datetime

app = Flask(__name__)

def extract_user_id(ticket):
    return ticket[:16].replace("'", "")

@app.route('/api/photon', methods=['POST'])
def photon_api():
    data = request.json
    ticket_value = data.get('Ticket', '')
    user_id = extract_user_id(ticket_value)
    data["UserId"] = user_id
    nonce = data["Nonce"]
    data["timestamp"] = datetime.utcnow().isoformat()
    print(data)
    return jsonify({
        "ResultCode": 1,
        "UserId": user_id
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
