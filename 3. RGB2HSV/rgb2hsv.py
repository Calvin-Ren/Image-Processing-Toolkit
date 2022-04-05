import os

def rgb_hsv(R,G,B):
    try:
        R_prime=R/255
        G_prime=G/255
        B_prime=B/255
        C_max=max(R_prime,G_prime,B_prime)
        C_min=min(R_prime,G_prime,B_prime)
        delta=C_max-C_min
        if delta==0:
            H=0
        elif C_max==R_prime:
            H=60*(((G_prime-B_prime)/delta)%6)
        elif C_max==G_prime:
            H = 60 * (((B_prime - R_prime) / delta) +2)
        else:
            H = 60 * (((R_prime - G_prime) / delta) + 4)
        H=round(H)
        if C_max==0:
            S=0
        else:
            S=round(delta/C_max,2)
        V=round(C_max,2)
        return [H,S,V]
    except Exception as e:
        print("Input Error")

txt_dir = "E:\\renqixuan\DeepLabV3Plus-Pytorch-master\\analysis_tools\\rgb2hsv_result.txt"  #txt文件输出地址
result = open(txt_dir,"w")

with open("tot_result_rgb.txt","r") as f:
    print("Start processing~~~~~~")
    rgb_data = f.read()
    rgb_data_box = eval(rgb_data)
    for temp_arr in rgb_data_box:
        sec_result_arr = [0,0,0,0]
        pos = 0
        for temp_rgb in temp_arr:
            # print(rgb_hsv(temp_rgb[0], temp_rgb[1], temp_rgb[2]), end=",", file=result)
            result_arr = rgb_hsv(temp_rgb[0], temp_rgb[1], temp_rgb[2])
            sec_result_arr[pos] = result_arr
            pos += 1
            # print('[{}, {}, {}]'.format(result_arr[0],result_arr[1],result_arr[2]),end=',',file=result)
        print(sec_result_arr,end=',',file=result)
    print("well done")
result.close()




# input_rgb = [225, 237, 247]
# hsv_arr = rgb_hsv(input_rgb[0],input_rgb[1],input_rgb[2])
# print(hsv_arr)

