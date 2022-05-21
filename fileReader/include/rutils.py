import json
import base64
import os

def readjsFile(path):
    with open(path) as f:
        data = f.read()
    return json.loads(data)

def writejsFile(path, js):
    with open(path, 'w') as f:
        json.dump(js, f, ensure_ascii=False)

def readImage(path):
    with open(path, "rb") as img_file:
        B64string = base64.b64encode(img_file.read())
    return B64string

def readImages(path):
    files = []
    for name in os.listdir(path):
        if os.path.isfile(os.path.join(path, name)):
            files.append(name)
    images = []
    for name in files:
        images.append({"fileName": name, "imageData" : str(readImage(path + name))})
    return images
