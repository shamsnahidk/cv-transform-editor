import cv2
import numpy as np


def translate(image, tx, ty):
    h, w = image.shape[:2]
    matrix = np.float32([[1, 0, tx], [0, 1, ty]])
    transformed = cv2.warpAffine(image, matrix, (w, h))
    return transformed, matrix


def rotate(image, angle):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    transformed = cv2.warpAffine(image, matrix, (w, h))
    return transformed, matrix


def scale(image, fx, fy):
    matrix = np.float32([[fx, 0, 0], [0, fy, 0]])
    transformed = cv2.resize(image, None, fx=fx, fy=fy)
    return transformed, matrix


def shear(image, shx=0.0, shy=0.0):
    h, w = image.shape[:2]
    matrix = np.float32([[1, shx, 0], [shy, 1, 0]])
    transformed = cv2.warpAffine(image, matrix, (w, h))
    return transformed, matrix
