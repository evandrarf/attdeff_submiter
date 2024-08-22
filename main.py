from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SUBMITTER_URL = 'https://and.idcyberskills.com/api/v2/submit'
TOKEN = open('/tmp/token.txt', 'r').read().strip()

if not TOKEN:
    print("[-] Token not found")
    exit(1)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()['flag']
    
    res = requests.post(SUBMITTER_URL, json={'flags': data}, headers={'Authorization': f'Bearer {TOKEN}'})
    
    print("[+] Response:", res.json())
    
    return jsonify(res.json())
    
    

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0')
