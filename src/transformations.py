import cv2
import numpy as np


def translate(image, tx, ty):
    h, w = image.shape[:2]
    matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    return cv2.warpAffine(image, matrix, (w, h))


def rotate(image, angle):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    return cv2.warpAffine(image, matrix, (w, h))


def scale(image, fx, fy):
    return cv2.resize(image, None, fx=fx, fy=fy)


def shear(image, shx=0.0, shy=0.0):
    h, w = image.shape[:2]
    matrix = np.float32([[1, shx, 0], [shy, 1, 0]])
    return cv2.warpAffine(image, matrix, (w, h))
