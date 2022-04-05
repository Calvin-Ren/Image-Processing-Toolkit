import math
import os

hsv_arr = [[0, 0.05, 0.92], [3, 0.09, 0.94], [350, 0.25, 0.94], [350, 0.4, 0.89], [350, 0.32, 0.93], [354, 0.17, 0.93], [21, 0.06, 0.93], [18, 0.17, 0.97], [10, 0.17, 0.97], [8, 0.22, 0.95], [8, 0.26, 0.95], [5, 0.27, 0.93], [22, 0.19, 0.98], [26, 0.25, 0.99], [24, 0.31, 0.98], [21, 0.3, 0.98], [19, 0.28, 0.92], [20, 0.31, 0.93], [30, 0.03, 0.93], [33, 0.16, 0.95], [32, 0.25, 0.99], [31, 0.32, 1.0], [29, 0.33, 0.99], [30, 0.4, 1.0], [50, 0.03, 0.91], [35, 0.17, 0.96], [32, 0.26, 0.95], [32, 0.24, 0.91], [32, 0.32, 0.93], [31, 0.21, 0.87], [35, 0.1, 0.94], [32, 0.12, 0.95], [33, 0.17, 0.98], [34, 0.14, 0.93], [29, 0.21, 0.89], [29, 0.21, 0.85], [49, 0.07, 0.95], [37, 0.12, 0.96], [40, 0.11, 0.96], [30, 0.01, 0.94], [87, 0.04, 0.94], [80, 0.03, 0.92], [71, 0.07, 0.93], [99, 0.08, 0.95], [108, 0.11, 0.93], [87, 0.13, 0.9], [71, 0.16, 0.84], [96, 0.15, 0.87], [143, 0.1, 0.95], [116, 0.12, 0.89], [133, 0.16, 0.87], [139, 0.18, 0.87], [151, 0.22, 0.87], [154, 0.26, 0.89], [163, 0.14, 0.89], [171, 0.17, 0.87], [165, 0.19, 0.85], [172, 0.27, 0.89], [181, 0.29, 0.87], [186, 0.3, 0.87], [159, 0.06, 0.92], [184, 0.12, 0.88], [196, 0.28, 0.91], [190, 0.28, 0.88], [194, 0.25, 0.85], [197, 0.31, 0.85], [196, 0.05, 0.89], [197, 0.15, 0.91], [204, 0.16, 0.92], [208, 0.26, 0.9], [204, 0.26, 0.85], [199, 0.2, 0.81], [7, 0.03, 0.93], [322, 0.09, 0.87], [332, 0.1, 0.92], [328, 0.15, 0.92], [328, 0.14, 0.89], [312, 0.11, 0.83], [10, 0.13, 0.89], [8, 0.23, 0.89], [5, 0.39, 0.9], [4, 0.44, 0.67], [2, 0.4, 0.78], [5, 0.31, 0.87], [19, 0.2, 0.91], [15, 0.3, 0.93], [12, 0.47, 0.92], [11, 0.56, 0.78], [12, 0.56, 0.92], [15, 0.39, 0.93], [32, 0.23, 0.91], [29, 0.37, 0.94], [27, 0.55, 0.96], [26, 0.63, 0.83], [26, 0.61, 0.95], [28, 0.46, 0.94], [38, 0.23, 0.9], [37, 0.34, 0.91], [36, 0.55, 0.96], [34, 0.63, 0.84], [35, 0.63, 0.96], [36, 0.45, 0.92], [44, 0.12, 0.95], [43, 0.21, 0.95], [42, 0.44, 1.0], [41, 0.61, 0.99], [42, 0.51, 1.0], [43, 0.32, 0.97], [108, 0.04, 0.93], [144, 0.09, 0.92], [152, 0.28, 0.88], [158, 0.51, 0.75], [156, 0.4, 0.79], [148, 0.17, 0.91], [160, 0.05, 0.92], [175, 0.1, 0.91], [175, 0.3, 0.88], [176, 0.71, 0.74], [176, 0.46, 0.77], [172, 0.19, 0.89], [175, 0.05, 0.92], [185, 0.11, 0.91], [189, 0.35, 0.87], [190, 0.69, 0.8], [190, 0.48, 0.86], [187, 0.22, 0.89], [192, 0.04, 0.91], [194, 0.09, 0.91], [201, 0.32, 0.89], [201, 0.59, 0.85], [203, 0.43, 0.9], [199, 0.21, 0.91], [200, 0.03, 0.91], [210, 0.07, 0.92], [217, 0.2, 0.9], [220, 0.43, 0.82], [220, 0.34, 0.86], [214, 0.15, 0.91], [14, 0.16, 0.77], [7, 0.26, 0.79], [4, 0.35, 0.68], [3, 0.37, 0.48], [4, 0.36, 0.58], [5, 0.33, 0.78], [18, 0.19, 0.8], [15, 0.3, 0.8], [13, 0.42, 0.71], [12, 0.45, 0.52], [11, 0.43, 0.62], [13, 0.41, 0.82], [20, 0.09, 0.94], [28, 0.36, 0.82], [27, 0.48, 0.73], [25, 0.48, 0.54], [25, 0.5, 0.65], [26, 0.47, 0.83], [37, 0.22, 0.78], [35, 0.33, 0.8], [34, 0.46, 0.72], [31, 0.49, 0.53], [33, 0.49, 0.61], [36, 0.45, 0.82], [28, 0.12, 0.88], [26, 0.12, 0.78], [22, 0.22, 0.62], [21, 0.26, 0.46], [20, 0.24, 0.54], [21, 0.22, 0.69], [12, 0.07, 0.86], [10, 0.06, 0.76], [10, 0.15, 0.6], [8, 0.19, 0.45], [8, 0.18, 0.51], [5, 0.14, 0.66], [347, 0.05, 0.75], [351, 0.04, 0.67], [333, 0.07, 0.51], [338, 0.08, 0.37], [338, 0.07, 0.44], [334, 0.05, 0.57], [69, 0.06, 0.86], [82, 0.06, 0.75], [90, 0.11, 0.56], [97, 0.12, 0.41], [95, 0.1, 0.48], [76, 0.12, 0.64], [113, 0.04, 0.85], [140, 0.05, 0.75], [161, 0.13, 0.56], [161, 0.15, 0.42], [159, 0.14, 0.48], [145, 0.1, 0.65], [185, 0.05, 0.86], [194, 0.07, 0.75], [196, 0.16, 0.58], [195, 0.18, 0.43], [196, 0.17, 0.5], [197, 0.15, 0.65], [347, 0.36, 0.91], [350, 0.49, 0.87], [353, 0.58, 0.82], [357, 0.71, 0.75], [354, 0.64, 0.79], [348, 0.44, 0.89], [9, 0.35, 0.85], [9, 0.46, 0.77], [8, 0.49, 0.73], [11, 0.62, 0.58], [9, 0.6, 0.63], [9, 0.41, 0.82], [42, 0.33, 1.0], [41, 0.53, 1.0], [37, 0.77, 0.96], [40, 0.57, 1.0], [42, 0.61, 0.96], [45, 0.44, 0.96], [159, 0.62, 0.73], [160, 0.61, 0.64], [161, 0.7, 0.54], [160, 0.62, 0.37], [166, 1.0, 0.42], [124, 1.0, 0.59], [201, 0.88, 0.73], [200, 1.0, 0.71], [200, 1.0, 0.53], [202, 0.76, 0.38], [198, 1.0, 0.44], [200, 1.0, 0.61], [240, 0.04, 0.2], [215, 0.14, 0.33], [60, 0.01, 0.4], [206, 0.06, 0.47], [206, 0.12, 0.53], [60, 0.01, 0.54], [197, 0.04, 0.61], [40, 0.02, 0.67], [202, 0.06, 0.74], [207, 0.04, 0.79], [195, 0.02, 0.85], [140, 0.01, 0.9]]


def color_match(input_hsv,hsv_arr):
    min_value = 255
    min_hsv_arr = []
    h = input_hsv[0]/360
    s = input_hsv[1]
    v = input_hsv[2]
    for temp_arr in hsv_arr:
        h_ = temp_arr[0]/360
        s_ = temp_arr[1]
        v_ = temp_arr[2]
        d_1 = abs(s*v*math.cos(2*math.pi*h) - s_*v_*math.cos(2*math.pi*h_))
        d_2 = abs(v*s*math.sin(2*math.pi*h) - v_*s_*math.sin(2*math.pi*h_))
        d_3 = abs(v - v_)
        dis = pow(d_1*d_1 + d_2*d_2 + d_3*d_3, 1/3)
        if (dis < min_value):
            min_value = dis
            min_hsv_arr = temp_arr
    return min_hsv_arr

txt_dir = "E:\\renqixuan\DeepLabV3Plus-Pytorch-master\\analysis_tools\\color_matching_result.txt"  #txt文件输出地址
result = open(txt_dir,"w")

with open("rgb2hsv_result.txt","r") as f:
    print("Start processing~~~~~~")
    hsv_data = f.read()
    hsv_data_box = eval(hsv_data)
    for temp_arr in hsv_data_box:
        sec_result_arr = [0, 0, 0, 0]
        pos = 0
        for temp_hsv in temp_arr:
            # print(rgb_hsv(temp_rgb[0], temp_rgb[1], temp_rgb[2]), end=",", file=result)
            result_arr = color_match(temp_hsv,hsv_arr)
            sec_result_arr[pos] = result_arr
            pos += 1
            # print('[{}, {}, {}]'.format(result_arr[0],result_arr[1],result_arr[2]),end=',',file=result)
        print(sec_result_arr, end=',', file=result)
    print("well done")


result.close()