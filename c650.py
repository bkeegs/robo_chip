import numpy as np
import cv2

class Camera(object):
    """An emulated camera implementation that streams a repeated sequence of
    files 1.jpg, 2.jpg and 3.jpg at a rate of one frame per second."""

    def __init__(self):
        self.cap = cv2.VideoCapture(1)
        ret, frame = self.cap.read()
        filename = './recent_frame.jpg'
        cv2.imwrite(filename, frame)

    def get_frame(self):
        ret, frame = self.cap.read()
        filename = './recent_frame.jpg'
        cv2.imwrite(filename, frame)
        return open(filename, 'rb').read()
