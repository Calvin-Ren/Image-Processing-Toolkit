from PIL import Image
import os
from collections import namedtuple


#语义分割类别,将 Cityscapes.py 的代码粘贴过来
CityscapesClass = namedtuple('CityscapesClass', ['name', 'id', 'train_id', 'category', 'category_id', 'has_instances', 'ignore_in_eval', 'color'])
classes = [
        CityscapesClass('unlabeled', 0, 255, 'void', 0, False, True, (0, 0, 0)),
        CityscapesClass('ego vehicle', 1, 255, 'void', 0, False, True, (0, 0, 0)),
        CityscapesClass('rectification border', 2, 255, 'void', 0, False, True, (0, 0, 0)),
        CityscapesClass('out of roi', 3, 255, 'void', 0, False, True, (0, 0, 0)),
        CityscapesClass('static', 4, 255, 'void', 0, False, True, (0, 0, 0)),
        CityscapesClass('dynamic', 5, 255, 'void', 0, False, True, (111, 74, 0)),
        CityscapesClass('ground', 6, 255, 'void', 0, False, True, (81, 0, 81)),
        CityscapesClass('road', 7, 0, 'flat', 1, False, False, (128, 64, 128)),
        CityscapesClass('sidewalk', 8, 1, 'flat', 1, False, False, (244, 35, 232)),
        CityscapesClass('parking', 9, 255, 'flat', 1, False, True, (250, 170, 160)),
        CityscapesClass('rail track', 10, 255, 'flat', 1, False, True, (230, 150, 140)),
        CityscapesClass('building', 11, 2, 'construction', 2, False, False, (70, 70, 70)),
        CityscapesClass('wall', 12, 3, 'construction', 2, False, False, (102, 102, 156)),
        CityscapesClass('fence', 13, 4, 'construction', 2, False, False, (190, 153, 153)),
        CityscapesClass('guard rail', 14, 255, 'construction', 2, False, True, (180, 165, 180)),
        CityscapesClass('bridge', 15, 255, 'construction', 2, False, True, (150, 100, 100)),
        CityscapesClass('tunnel', 16, 255, 'construction', 2, False, True, (150, 120, 90)),
        CityscapesClass('pole', 17, 5, 'object', 3, False, False, (153, 153, 153)),
        CityscapesClass('polegroup', 18, 255, 'object', 3, False, True, (153, 153, 153)),
        CityscapesClass('traffic light', 19, 6, 'object', 3, False, False, (250, 170, 30)),
        CityscapesClass('traffic sign', 20, 7, 'object', 3, False, False, (220, 220, 0)),
        CityscapesClass('vegetation', 21, 8, 'nature', 4, False, False, (107, 142, 35)),
        CityscapesClass('terrain', 22, 9, 'nature', 4, False, False, (152, 251, 152)),
        CityscapesClass('sky', 23, 10, 'sky', 5, False, False, (70, 130, 180)),
        CityscapesClass('person', 24, 11, 'human', 6, True, False, (220, 20, 60)),
        CityscapesClass('rider', 25, 12, 'human', 6, True, False, (255, 0, 0)),
        CityscapesClass('car', 26, 13, 'vehicle', 7, True, False, (0, 0, 142)),
        CityscapesClass('truck', 27, 14, 'vehicle', 7, True, False, (0, 0, 70)),
        CityscapesClass('bus', 28, 15, 'vehicle', 7, True, False, (0, 60, 100)),
        CityscapesClass('caravan', 29, 255, 'vehicle', 7, True, True, (0, 0, 90)),
        CityscapesClass('trailer', 30, 255, 'vehicle', 7, True, True, (0, 0, 110)),
        CityscapesClass('train', 31, 16, 'vehicle', 7, True, False, (0, 80, 100)),
        CityscapesClass('motorcycle', 32, 17, 'vehicle', 7, True, False, (0, 0, 230)),
        CityscapesClass('bicycle', 33, 18, 'vehicle', 7, True, False, (119, 11, 32)),
        CityscapesClass('license plate', -1, 255, 'vehicle', 7, False, True, (0, 0, 142)),
]

#txt输出
txt_dir = "E:\\renqixuan\DeepLabV3Plus-Pytorch-master\\analysis_tools\\txt_result.txt"  #txt文件输出地址
result = open(txt_dir, "w")


# 分类类型输出
for c in classes:
    print(c.name, end=",", file=result)
print(file=result)


files_dir = "E:\\renqixuan\DeepLabV3Plus-Pytorch-master\\test_results"  #添加文件位置

for root, dirs, files in os.walk(files_dir):
    for img_name in files:
        img = Image.open(files_dir+"/"+img_name)

        #输出图片id
        name_box = img_name.split(".")
        img_id = name_box[0]
        print(img_id,end=",",file=result)

        #获取图片大小
        width = img.size[0]  # 长度
        height = img.size[1]  # 宽度

        # 以下是类别的检测代码
        total_pixel = 1
        select_pixel = 1

        for c in classes:
            if (c.ignore_in_eval == True):
                print(0, end=",", file=result)
            else:
                for i in range(0,width):
                    for j in range(0, height):
                        data = (img.getpixel((i, j)))  # 打印该图片的所有点
                        R = data[0]
                        G = data[1]
                        B = data[2]
                        total_pixel += 1

                        #读取标签颜色数据
                        img_R = c.color[0]
                        img_G = c.color[1]
                        img_B = c.color[2]
                        if (R == img_R and G == img_G and B == img_B):  # 红色的区域取值，根据不同需求，这里的数值可以变化，主要用于设置色彩范围
                            select_pixel += 1
                select_data = select_pixel / total_pixel  # 红色的数据
                print(select_data, end=",", file=result)

        print(file=result)

result.close()


