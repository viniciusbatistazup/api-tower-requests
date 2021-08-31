# encoding: utf-8
import json
import logging
import socket
from flask import Flask, request
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from prometheus_flask_exporter import PrometheusMetrics
# from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics

app = Flask(__name__)

metrics = PrometheusMetrics(app)

app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})

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


@app.route('/hello')
def hello():
    return json.dumps({'msg': 'Hello !'}), 200


@app.route('/debug')
def debug():
    logging.debug(' debug')
    logging.info(' info')
    logging.warning(' warning')
    logging.error(' error')
    logging.critical(' critical')
    return json.dumps({'msg': 'Debug !'}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
