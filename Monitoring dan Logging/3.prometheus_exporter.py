from flask import Flask, Response
from prometheus_client import CollectorRegistry, Gauge, generate_latest
import psutil
import random

app = Flask(__name__)
registry = CollectorRegistry()

model_latency = Gauge('model_latency_seconds', 'Latensi prediksi model', registry=registry)
model_accuracy = Gauge('model_accuracy', 'Akurasi model', registry=registry)
cpu_usage = Gauge('system_cpu_usage', 'Persentase penggunaan CPU', registry=registry)

@app.route('/metrics')
def metrics():
    model_latency.set(random.uniform(0.01, 0.05)) 
    model_accuracy.set(0.95)
    cpu_usage.set(psutil.cpu_percent())
    return Response(generate_latest(registry), mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)