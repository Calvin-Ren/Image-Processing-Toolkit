import cv2 as cv
# import tkinter
from matplotlib import pyplot as plt
import os.path
from os import path
import glob


# simple function for split hist in n part
# view doc for example how the function split the array
def splitHist(nPart, hist):
    totalP = sum(hist)[0]
    # print((hist[0]))
    # print('totalP:')
    # print(totalP)
    newArray = []
    lPartInt, lPartDec = divmod((len(hist) / nPart), 1)
    lPartInt = (int(lPartInt))
    lPartDec = (int(lPartDec * nPart))
    i = 0
    # i want to make a PARTITOIN but i want to take de decimal value of division in a central part for don't influence the extreme part
    if (nPart % 2 == 0):
        extraPartIndex = int(nPart / 2) - 1
    else:
        extraPartIndex = int(nPart / 2)
    while (i < 256):
        if (i == extraPartIndex * lPartInt):
            newArray.append(((sum(hist[i: i + lPartInt + lPartDec])[0]) / totalP))
            i += lPartInt
            i += lPartDec
        newArray.append(((sum(hist[i: i + lPartInt])[0]) / totalP))
        i += lPartInt

    # the sum must be ~ 1
    return (newArray)


def decideExposition(fileDir):
    if (path.isfile(fileDir)):
        img = cv.imread(fileDir, 0)
        hist = cv.calcHist([img], [0], None, [256], [0, 256])
        ##view plot rappresentation
        # plt.hist(img.ravel(),256,[0,256]);
        # plt.show()
        split = (splitHist(10, hist))
        restDx = 0
        restSx = 0
        for i, s in enumerate(split):
            if i != 0 and i != 1:
                restDx += s
            if i != len(split) - 1 and i != len(split) - 2:
                restSx += s
        if split[0] + split[1] > restDx and split[len(split) - 1] == 0.0:

            return 0
        elif (split[len(split) - 1] + (split[len(split) - 2] > restSx) and (split[0]) == 0.0):

            return 1
        else:

            return 0
    else:
        return ('path is not a file')

file_dir = "E:\\renqixuan\DeepLabV3Plus-Pytorch-master\datasets\img_set\over-exposed_img/"
image_files = glob.glob(os.path.join(file_dir,"*.jpg"))

#print(image_files)

for img in image_files:
    #print(img)
    fileDir = img
    decideExposition(fileDir)
    if (decideExposition(fileDir)):
        os.remove(fileDir)
        print("Removed image:" + fileDir)
    else:
        continue

print("Succeed")


