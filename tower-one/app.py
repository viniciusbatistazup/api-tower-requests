import requests
import time
import sys
import logging
import os
from load_conf import load_yml_file

tower_one_endpoint = os.getenv('TOWER_ONE_ENDPOINT', 'localhost')
tower_one_port = os.getenv('TOWER_ONE_PORT', '5000')
tower_one_interval_request = os.getenv('TOWER_ONE_INTERVAL_REQUEST', '0.05')

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',  level=logging.INFO)


yml = load_yml_file("conf.yaml")


def calc_requests(yml):
    for item, url in yml.items():

        try:
            status200 = (url["2xx"])
        except:
            status200 = 0

        try:
            status300 = (url["3xx"])
        except:
            status300 = 0

        try:
            status400 = (url["4xx"])
        except:
            status400 = 0

        try:
            status500 = (url["5xx"])
        except:
            status500 = 0

        logging.info('status200: '+str(status200))
        logging.info('status300: '+str(status300))
        logging.info('status400: '+str(status400))
        logging.info('status500: '+str(status500))

        # print(status200)
        # print(status300)
        # print(status400)
        # print(status500)

        sum_total_status_code = status200 + status300 + status400 + status500
        logging.info('sum_total_status_code: '+str(sum_total_status_code))
        # print(sum_total_status_code)

        if(sum_total_status_code != 100):
            print('Invalid conf.yaml\nsum(num_requests) should give 100')
            sys.exit(1)

        send_requests(status200, 200)
        send_requests(status300, 300)
        send_requests(status400, 400)
        send_requests(status500, 500)


def send_requests(number, path):

    for x in range(number):

        try:
            requests.get(
                'http://'+str(tower_one_endpoint)+':'+str(tower_one_port)+'/'+str(path)
            )
            time.sleep(0.1)
        except:
            logging.error('Request error %s:%s', str(tower_one_endpoint), str(tower_one_port))


while True:
    calc_requests(yml)
    time.sleep(float(tower_one_interval_request))
