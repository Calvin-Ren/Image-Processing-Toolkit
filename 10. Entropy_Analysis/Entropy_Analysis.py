from skimage.measure.entropy import shannon_entropy
from skimage import io
import os


def get_entropy(img):
    iEntropy = shannon_entropy(img[:, :, 0])
    return iEntropy


def img_analysis():
    img_files_dir = "E:\\renqixuan\DeepLabV3Plus-Pytorch-master\datasets\img_set\\test_files"
    for root, dirs, files in os.walk(img_files_dir):
        for img_name in files:
            img_dir = img_files_dir + "\\" + img_name
            img = io.imread(img_dir)
            temp_value = get_entropy(img)
            temp_name = img_name.split('.jpg')[0]
            print(str(temp_name) + ":  " + str(temp_value))


def main():
    img_analysis()


if __name__ == "__main__":
    main()

