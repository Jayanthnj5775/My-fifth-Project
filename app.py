from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Python Kubernetes & CI/CD App is running!"

@app.route("/status")
def status():
    return jsonify({"service": "python-k8s-api", "ok": True}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
