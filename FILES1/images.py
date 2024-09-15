!pip install opencv-python matplotlib

import cv2

image = cv2.imread("image1.jpeg") 


cv2.imshow('Loaded Image', image)


cv2.waitKey(0)
cv2.destroyAllWindows()
