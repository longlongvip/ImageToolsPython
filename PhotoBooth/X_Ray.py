import cv2
import numpy as np


def x_ray(image):
    """
    Make Image X-Ray Style
    :param image: numpy.ndarray
    :return: image's style like X-Ray
    """
    h, w, c = image.shape
    global image_gray
    if c == 3:
        image_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif c == 1:
        image_gray = image
    else:
        print("Image Error")
    res = np.zeros((h, w), np.uint8)
    for i in range(h):
        for j in range(w):
            res[i][j] = 255 - image_gray[i][j]
    return res


img = cv2.imread("ZS.jpg")
img_X_ray = x_ray(img)
cv2.imshow("X-Ray Style", img_X_ray)
cv2.waitKey()
