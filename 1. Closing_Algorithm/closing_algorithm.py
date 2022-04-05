import cv2
import numpy as np
o=cv2.imread("E:\\renqixuan\DeepLabV3Plus-Pytorch-master\\test_results_01\\116.407825,39.93167_90.png",cv2.IMREAD_UNCHANGED)
k=np.ones((12,12),np.uint8)
r=cv2.morphologyEx(o,cv2.MORPH_CLOSE,k)
cv2.imwrite("E:\\renqixuan\DeepLabV3Plus-Pytorch-master\datasets\img_set\copy_test\\result.png",r)
cv2.imshow("original",o)
cv2.imshow("result",r)
cv2.waitKey()
cv2.destroyAllWindows()
