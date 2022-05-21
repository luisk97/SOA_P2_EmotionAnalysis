
import os

from google.cloud import vision

KEY = './key.json'

os.environ['GOOGLE_APPLICATION_CREDENTIALS']=KEY

vision_client = vision.ImageAnnotatorClient()

def visionResponse(data):
    response = []
    for image in data:
        img_data = image["imageData"][2:]
        img_data = img_data[:len(img_data)-1]
        image_vision = vision.Image(content=img_data)
        face_response = vision_client.face_detection(image=image_vision)
        for face_detection in face_response.face_annotations:
            analysis={
                'joy': face_detection.joy_likelihood,
                'sorrow': face_detection.sorrow_likelihood,
                'surprise': face_detection.surprise_likelihood,
                'anger': face_detection.anger_likelihood,
                'fileName': image["fileName"]
            }
            response.append(analysis)
    return response