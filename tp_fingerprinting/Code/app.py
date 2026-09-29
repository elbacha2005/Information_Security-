from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():    
    print("IP address :", request.remote_addr)
    print("HTTP methode :", request.method)
    
    print("User Agent :", request.headers.get('User-Agent'))
    print("Accept-Language :", request.headers.get('Accept-Language'))
    
    print("Accept          :", request.headers.get("Accept"))
    print("Accept-Encoding :", request.headers.get("Accept-Encoding"))
    print("Sec-Fetch-Site  :", request.headers.get("Sec-Fetch-Site"))
    print("DNT             :", request.headers.get("DNT"))
    
    return render_template('index.html')

@app.route("/collect", methods=["POST"])
def collect():
    data = request.get_json()
    print("\n===== DATA RECEIVED =====")
    for key, value in data.items():
        print(f"{key}: {value}")
    print("=========================\n")
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)