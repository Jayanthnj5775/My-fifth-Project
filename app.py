from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Python Kubernetes & CI/CD App v2 - Automated Rollout!"

@app.route("/status")
def status():
    return jsonify({"service": "python-k8s-api", "version": "v2", "ok": True}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
