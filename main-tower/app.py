# encoding: utf-8
import json
from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)

metrics = PrometheusMetrics(app)


@app.route('/200')
def success():
    return json.dumps({'status-code': '200'}), 200


@app.route('/300')
def index():
    return json.dumps({'status-code': '300'}), 300


@app.route('/400')
def redirect():
    return json.dumps({'status-code': '400'}), 400


@app.route('/500')
def server():
    return json.dumps({'status-code': '500'}), 500


@app.route('/division')
def division():
    return 1/0

app.run()
