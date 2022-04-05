#
#  Use k-means clustering to find the most-common colors in an image
#
import cv2
import os
import numpy as np
from sklearn.cluster import KMeans


def make_histogram(cluster):
    """
    Count the number of pixels in each cluster
    :param: KMeans cluster
    :return: numpy histogram
    """
    numLabels = np.arange(0, len(np.unique(cluster.labels_)) + 1)

    hist, _ = np.histogram(cluster.labels_, bins=numLabels)

    hist = hist.astype('float32')
    hist /= hist.sum()
    return hist


def make_bar(height, width, color):
    """
    Create an image of a given color
    :param: height of the image
    :param: width of the image
    :param: BGR pixel values of the color
    :return: tuple of bar, rgb values, and hsv values
    """
    bar = np.zeros((height, width, 3), np.uint8)
    bar[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    hsv_bar = cv2.cvtColor(bar, cv2.COLOR_BGR2HSV)
    hue, sat, val = hsv_bar[0][0]
    return bar, (red, green, blue), (hue, sat, val)


def sort_hsvs(hsv_list):

    """
    Sort the list of HSV values
    :param hsv_list: List of HSV tuples
    :return: List of indexes, sorted by hue, then saturation, then value
    """

    bars_with_indexes = []
    for index, hsv_val in enumerate(hsv_list):
        bars_with_indexes.append((index, hsv_val[0], hsv_val[1], hsv_val[2]))
    bars_with_indexes.sort(key=lambda elem: (elem[1], elem[2], elem[3]))
    return [item[0] for item in bars_with_indexes]

#txt输出
txt_dir = "E:\\renqixuan\DeepLabV3Plus-Pytorch-master\\analysis_tools\\rgb_result.txt"  #txt文件输出地址
tot_result = open("E:\\renqixuan\DeepLabV3Plus-Pytorch-master\\analysis_tools\\tot_result_rgb.txt", "w")
result = open(txt_dir, "w")

# START HERE
files_dir = "E:\\renqixuan\DeepLabV3Plus-Pytorch-master\\datasets\\img_set\\east_city_district_seg_cleaned"  #添加文件位置
total_num = 13227
cur_num = 1
for root, dirs, files in os.walk(files_dir):
    for img_name in files:
        img = cv2.imread(files_dir+"\\"+img_name)
# img = cv2.imread('E:\\renqixuan\DeepLabV3Plus-Pytorch-master\datasets\img_set\\116.407825,39.93167_90.jpg')
        height, width, _ = np.shape(img)

# reshape the image to be a simple list of RGB pixels

# image = img.reshape((height * width, 3))
# image=image[image!=[0,0,0]]
# image = image.reshape((len(image), 3))
# create the indices that have at least one channel of the pixel different than 0
        indToSelect = np.all(img != [0,0,0], keepdims=True, axis=2)[:,:,0] # used [:,:,0] because numpy returns an array of shape (rows, cols, 1)
        # get the 3 channel values of the selected values above
        image = img[indToSelect, :]


# we'll pick the 4 most common colors
        num_clusters = 4
        clusters = KMeans(n_clusters=num_clusters)
        clusters.fit(image)

# count the dominant colors and put them in "buckets"
        histogram = make_histogram(clusters)
        # then sort them, most-common first
        combined = zip(histogram, clusters.cluster_centers_)
        combined = sorted(combined, key=lambda x: x[0], reverse=True)

        # finally, we'll output a graphic showing the colors in order
        bars = []
        hsv_values = []
        rgb_values = []
        for index, rows in enumerate(combined):
            bar, rgb, hsv = make_bar(100, 100, rows[1])
            # print(f'Bar {index + 1}')
            # print(f'  RGB values: {rgb}')
            # print(f'  HSV values: {hsv}')
            rgb_values.append(rgb)
            hsv_values.append(hsv)
            bars.append(bar)

        # sort the bars[] list so that we can show the colored boxes sorted
        # by their HSV values -- sort by hue, then saturation
        sorted_bar_indexes = sort_hsvs(hsv_values)
        sorted_bars = [bars[idx] for idx in sorted_bar_indexes]
        # print(sorted_bar_indexes)
        # print(hsv_values)
        # print("sorted rgb:")
        result_arr = [0,0,0,0]
        for i in range(0,4):
            result_arr[sorted_bar_indexes[i]] = rgb_values[i]
        print(result_arr,end=",", file=tot_result)
        print(img_name,":",result_arr,file=result)
        print("Current stage: ",cur_num,"/",total_num)
        cur_num += 1

    print("done")
    result.close()

        # cv2.imshow('Sorted by HSV values', np.hstack(sorted_bars))
        # cv2.imshow(f'{num_clusters} Most Common Colors', np.hstack(bars))
        # cv2.waitKey(0)