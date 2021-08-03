import requests
import time
import sys
from load_conf import load_yml_file


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

        print(status200)
        print(status300)
        print(status400)
        print(status500)

        sum_total_status_code = status200 + status300 + status400 + status500
        print(sum_total_status_code)
        if(sum_total_status_code is not 100):
            print('Invalid conf.yaml\nsum(num_requests) should give 100')
            sys.exit(1)

        send_requests(status200, 200)
        send_requests(status300, 300)
        send_requests(status400, 400)
        send_requests(status500, 500)


def send_requests(number, path):
    
    for x in range(number):  
        requests.get(
            'http://localhost:5000/'+str(path)
        )
        time.sleep(0.1)


while True:
    calc_requests(yml)
    time.sleep(0.1)
