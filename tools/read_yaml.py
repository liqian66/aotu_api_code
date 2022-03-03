import os

import yaml
from yaml import FullLoader

from config import BASE_PATH

# 定义列表，将读取到的数据组装到列表
arr = []


def read_yaml_data(filename):
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(file_path, "r", encoding="utf-8") as f:
        for datas in yaml.load(f, Loader=FullLoader).values():
            arr.append(datas.values())
    print(arr)
    return arr


if __name__ == '__main__':
    read_yaml_data("login.yaml")
