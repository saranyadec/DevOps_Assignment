from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Minikube Kubernetes!"

@app.route("/cpu")
def cpu_stress():
    # simulate CPU load
    for i in range(10000000):
        i*i
    return "CPU task completed!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
