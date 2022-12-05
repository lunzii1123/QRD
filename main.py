import cv2
import numpy as np
import json
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


def draw_square(barcode):
    pts = np.array([barcode.polygon], np.int32)
    pts = pts.reshape((-1, 1, 2))
    cv2.polylines(image, [pts], True, (255, 0, 255), 5)


def is_valid_json(myjson):
    try:
        json.loads(myjson)
    except ValueError as e:
        return False
    return True


def read_qr_code(image):
    for barcode in decode(image):
        draw_square(barcode)
        data_in_qr_code = barcode.data.decode('utf-8')
        return data_in_qr_code


while True:
    is_success, image = cap.read()
    returned_value = read_qr_code(image)
    print(returned_value)
    print(is_valid_json(returned_value))

    cv2.imshow('Realtime QR code detector', image)
    cv2.waitKey(20)
