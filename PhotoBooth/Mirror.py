import cv2
import numpy as np


def h_mirror(image):
    """
    Mirror the image horizontally
    :param image: numpy.ndarray
    :return: Vertical mirror image
    """
    h, w, c = image.shape
    res = np.zeros((h, w, c), np.uint8)
    for i in range(h):
        for j in range(w):
            res[i][j] = image[i][w - 1 - j]
    return res


def v_mirror(image):
    """
    Make the image mirror vertically.
    :param image: numpy.ndarray
    :return: Vertical mirror image
    """
    h, w, c = image.shape
    res = np.zeros((h, w, c), np.uint8)
    for i in range(h):
        for j in range(w):
            res[i][j] = image[h - 1 - i][j]
    return res


def d_mirror(image):
    """
    Mirror the image diagonally.
    :param image: numpy.ndarray
    :return: Diagonal mirror image
    """
    h, w, c = image.shape
    res = np.zeros((h, w, c), np.uint8)
    for i in range(h):
        for j in range(w):
            res[i][j] = image[h - 1 - i][w - 1 - j]
    return res


def merge_h(image, image_h):
    """

    :param image:
    :param image_h:
    :return:
    """
    h, w, c = image.shape
    res = np.zeros((h, w, c), np.uint8)
    for i in range(h):
        for j in range(w):
            if j < w/2:
                res[i][j] = image[i][j]
            else:
                res[i][j] = image_h[i][j]
    return res


def merge_v(image, image_v):
    """

    :param image:
    :param image_v:
    :return:
    """
    h, w, c = image.shape
    res = np.zeros((h, w, c), np.uint8)
    for i in range(h):
        for j in range(w):
            if i < h/2:
                res[i][j] = image[i][j]
            else:
                res[i][j] = image_v[i][j]
    return res


def merge_d(image, image_d):
    """

    :param image:
    :param image_d:
    :return:
    """
    h, w, c = image.shape
    res = np.zeros((h, w, c), np.uint8)
    for i in range(h):
        for j in range(w):
            if w*i + h*j <= w*h:
                res[i][j] = image[i][j]
            else:
                res[i][j] = image_d[i][j]
    return res


img = cv2.imread("ZS.jpg")
img_mirror = d_mirror(img)
img_merge = merge_d(img, img_mirror)
cv2.imshow("Mirror Style", img_merge)
cv2.waitKey()
