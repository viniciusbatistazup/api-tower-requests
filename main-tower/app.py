# encoding: utf-8
import json
import logging
import os
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from prometheus_client import make_wsgi_app
from prometheus_client import Gauge, Counter
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)

metrics = PrometheusMetrics(app)
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})


IN_PROGRESS = Gauge("inprogress_requests", "Example gauge",
                    multiprocess_mode='livesum')
NUM_REQUESTS = Counter("num_requests", "Example counter")


@app.route("/")
@IN_PROGRESS.track_inprogress()
def home():
    NUM_REQUESTS.inc()
    return "pid: {}".format(os.getpid())


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
    return json.dumps({'msg': 'Debug !'}), 200


@app.route('/info')
def info():
    logging.info(' info')
    return json.dumps({'msg': 'Info !'}), 200


@app.route('/warning')
def warning():
    logging.warning(' warning')
    return json.dumps({'msg': 'Warning !'}), 200


@app.route('/critical')
def critical():
    logging.critical(' critical')
    return json.dumps({'msg': 'Critical !'}), 200


@app.route('/error')
def error():
    logging.error(' error')
    return json.dumps({'msg': 'Error !'}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0')
