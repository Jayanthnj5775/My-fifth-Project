from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "Python Kubernetes & CI/CD App - Monitored by Prometheus!"

@app.route("/status")
def status():
    return jsonify({"service": "python-k8s-api", "metrics_enabled": True, "ok": True}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
