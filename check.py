import os
import logging
import subprocess
import requests
import schedule
import time
from configparser import ConfigParser

parser = ConfigParser()
parser.read("./config.ini")    

def restart_apache():
    logging.info("Restarting apache")
    command = "/usr/sbin/httpd -d $HOME/apache -k restart"
    command_expanded = os.path.expandvars(command)
    subprocess.run(command_expanded)


def send_request():
    url = parser['url']['url']
    logging.info(f"Checking HTTP status at: {url}")
    response = requests.get(url)
    logging.info(f"Received status code {response.status_code}")
    if not response.ok:
        restart_apache()


if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s [%(levelname)s] %(message)s',
        level=logging.INFO,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    schedule.every().hour.do(send_request)
    logging.info("Starting checking job.")
    while True:
        schedule.run_pending()
        time.sleep(1)
