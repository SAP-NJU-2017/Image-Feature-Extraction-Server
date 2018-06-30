import zipfile
import json


def save_json(filename, json_str):
    with open(filename, "w") as f:
        new_dict = json.loads(json_str)
        json.dump(new_dict, f)
        print("加载入文件完成...")


def zip_files(files, zip_name):
    zip = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
    for file in files:
        print('compressing', file)
        zip.write(file)
    zip.close()
    print('compressing finished')

    # files = ['.\\123.txt', '.\\3.txt']  # 文件的位置，多个文件用“，”隔开
    # zip_file = '.\\m66y.zip'  # 压缩包名字
    # zip_files(files, zip_file)


if __name__ == "__main__":
    files =['../../doc/Vectors/1.png.json','../../doc/Vectors/2.png.json']
    zip_files(files,'test.zip')
