import cv2


def thermal_sensor(image):
    """
    Make Image thermal Style
    :param image: numpy.ndarray
    :return: image's style like thermal
    """
    h, w, _ = image.shape
    res = cv2.applyColorMap(image, cv2.COLORMAP_JET)
    return res


img = cv2.imread("ZS.jpg")
img_thermal = thermal_sensor(img)
cv2.imshow("Thermal Sensor Style", img_thermal)
cv2.waitKey()
