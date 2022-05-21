# pylint: disable=C0114
# pylint: disable=W0613
# pylint: disable=W0703
import signal

import time

import requests

DELAY = 10
URL = "http://file-reader-app-deploy:5000/readImages"

def handler(signum,stack):
    """SIGALRM handler, sends the request to fileReader"""
    try:
        requests.post(URL)
    except Exception as exception:
        print(str(exception))

def alarm():
    """Infinite loop, that sleeps a set time, and when done, sends the SIGALRM signal"""
    print("alarm service started")
    while 1:
        time.sleep(DELAY)
        signal.alarm(1) # pylint: disable=E1101

if __name__ == '__main__':
    try:
        signal.signal(signal.SIGALRM, handler)
    except Exception as error_signal:
        print(str(error_signal))
    print("signal registered")
    alarm()
