import cv2

img = cv2.imread('assets/cam.jpg', 1)
img = cv2.resize(img, (0, 0), fx=0.3, fy=0.3)
#img = cv2.rotate(img,cv2.ROTATE_180)

cv2.imwrite('new_Resize_img.jpg', img)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()