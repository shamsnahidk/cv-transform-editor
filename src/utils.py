import cv2
import numpy as np


def resize_to_same_height(img1, img2):
    h1, w1 = img1.shape[:2]
    h2, w2 = img2.shape[:2]

    target_height = min(h1, h2)

    new_w1 = int((target_height / h1) * w1)
    new_w2 = int((target_height / h2) * w2)

    resized1 = cv2.resize(img1, (new_w1, target_height))
    resized2 = cv2.resize(img2, (new_w2, target_height))

    return resized1, resized2


def stack_side_by_side(original, transformed):
    original_resized, transformed_resized = resize_to_same_height(original, transformed)
    combined = np.hstack((original_resized, transformed_resized))
    return combined


def add_labels(original, transformed):
    original_copy = original.copy()
    transformed_copy = transformed.copy()

    cv2.putText(
        original_copy,
        "Original",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )

    cv2.putText(
        transformed_copy,
        "Transformed",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
        cv2.LINE_AA,
    )

    return original_copy, transformed_copy
