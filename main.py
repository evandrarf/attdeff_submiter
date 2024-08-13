from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SUBMITTER_URL = 'http://172.31.8.194:5000/api/v2/submit'
TOKEN = ''

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()['flag']
    
    res = requests.post(SUBMITTER_URL, json={'flags': data}, headers={'Authorization': f'Bearer {TOKEN}'})
    
    print("[+] Response:", res.json())
    
    return jsonify(res.json())
    
    

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0')