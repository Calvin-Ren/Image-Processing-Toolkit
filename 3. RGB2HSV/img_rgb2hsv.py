import cv2


img_dir = "E:\\renqixuan\DeepLabV3Plus-Pytorch-master\datasets\img_set\\v2.jpg"
img = cv2.imread(img_dir)
hsv_bgr = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
hsvImg = cv2.cvtColor(hsv_bgr,cv2.COLOR_BGR2HSV)

cv2.imshow("Original img", img)
cv2.imshow("hsv img", hsvImg)

cv2.waitKey(0)
