import xlwt
from skimage.measure.entropy import shannon_entropy
from skimage import io
import os


def get_entropy(img):
    iEntropy = shannon_entropy(img[:, :, 0])
    return iEntropy


def data_saving(res_list):
    savepath = 'Entropy_result.xls'
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet('东城区熵', cell_overwrite_ok=True)
    col = ("location", "Entropy")
    for i in range(0, 2):
        sheet.write(0, i, col[i])
    for i in range(len(res_list)):
        print("-----No.%d is saving currently-----" % (i + 1))
        current_res = res_list[i]
        for j in range(0, 2):
            sheet.write(i + 1, j, current_res[j])

    book.save(savepath)


def img_analysis(res_list):
    img_files_dir = "E:\\renqixuan\DeepLabV3Plus-Pytorch-master\datasets\img_set\\east_city_district"
    for root, dirs, files in os.walk(img_files_dir):
        for img_name in files:
            temp = []  # stores name and entropy for current image
            img_dir = img_files_dir + "\\" + img_name
            img = io.imread(img_dir)
            temp_value = get_entropy(img)
            temp_name = img_name.split('.jpg')[0]
            temp.append(temp_name)
            temp.append(temp_value)

            res_list.append(temp)
            print(img_name + "--- analysis succeeded")

    return res_list


def main():
    res_list = []
    res_list = img_analysis(res_list)
    data_saving(res_list)
    print("---------Done")



if __name__ == "__main__":
    main()