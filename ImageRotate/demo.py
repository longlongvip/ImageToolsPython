import cv2


# mode:File or Folder
mode = "File"
# multi:rotate more angles or one angle
multi = True

theta_list = \
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
     21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
     39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
     57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70,  71, 72, 73, 74,
     75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90]
theta_10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def rotate_image(image, angle, center=None, scale=1.0):
    """

    :param image: image which you want to rotate
    :param angle: angle of rotate
    :param center: center of rotate
    :param scale:
    :return: image after rotate
    """
    # get size of image
    (h, w) = image.shape[:2]
    # If no rotation center is specified, the center of the image is set as the center of rotation
    if center is None:
        center = (w / 2, h / 2)
    # do rotate
    m = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, m, (w, h))
    # return the image rotated
    return rotated


if mode == "File":
    img = cv2.imread("ZGL.jpg")
    if multi:
        for i in range(1, 31):
            img_rotate = rotate_image(img, i)
            cv2.imwrite("./Result/" + "Rotate" + str(i) + ".jpg", img_rotate)
    else:
        # put in a angle
        theta = int(input())
        img_rotate = rotate_image(img, theta)
        cv2.imshow("Rotate" + str(theta), img_rotate)
        cv2.imwrite("Result/" + "Rotate" + str(theta) + ".jpg", img_rotate)
        cv2.waitKey()

if mode == "Folder":
    pass
