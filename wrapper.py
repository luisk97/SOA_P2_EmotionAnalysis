import os

import threading

import subprocess

import time

def codeCheck():
    print("----------Code Check-------------")
    print("Checking timer.py")
    os.system("cd timer && pylint timer.py")
    print("Checking fileReader.py")
    os.system("cd fileReader && pylint fileReader.py")
    print("Checking imageAnalysis.py")
    os.system("cd imgAnalysis && pylint imageAnalysis.py")
    print("Checking fileWriter.py")
    os.system("cd fileWriter && pylint fileWriter.py")
    print("----------End Code Check-------------")

def doPodWriter():
    os.system("cd fileWriter && docker build -f Dockerfile -t file-writer-app . && minikube image load file-writer-app:latest && kubectl create --filename deployment.yaml && kubectl expose deployment file-writer-app-deploy --type=NodePort --port=8000 && minikube service file-writer-app-deploy --url")

def doPodAnalysis():
    os.system("cd imgAnalysis && docker build -f Dockerfile -t analysis-app . && minikube image load analysis-app:latest && kubectl create --filename deployment.yaml && kubectl expose deployment analysis-app-deploy --type=NodePort --port=7000 && minikube service analysis-app-deploy --url")

def doPodReader():
    os.system("cd fileReader && docker build -f Dockerfile -t file-reader-app . && minikube image load file-reader-app:latest && kubectl create --filename deployment.yaml && kubectl expose deployment file-reader-app-deploy --type=NodePort --port=5000 && minikube service file-reader-app-deploy --url")

def doPodTimer():
    os.system("cd timer && docker build -f Dockerfile -t timer-app . && minikube image load timer-app:latest && kubectl create --filename deployment.yaml")

codeCheck()

os.system("minikube delete")
os.system("minikube start")

writeDeploy = threading.Thread(target=doPodWriter)
analysisDeploy = threading.Thread(target=doPodAnalysis)
readerDeploy = threading.Thread(target=doPodReader)
timerDeploy = threading.Thread(target=doPodTimer)

writeDeploy.start()
analysisDeploy.start()
readerDeploy.start()
time.sleep(10)
timerDeploy.start()

writeDeploy.join()
analysisDeploy.join()
readerDeploy.join()
timerDeploy.join()


##kubectl exec -it name -- bash
