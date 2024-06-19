import os
import cv2
import glob
import json
import numpy as np


def convert(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


class_names = ["nest", "kite", "ballon", "fire", "person", "monkey"]
out_dir = "G:/UAV/dataset/dataset1024/images2"
txt_dir = "G:/UAV/dataset/dataset1024/labels2"
os.makedirs(txt_dir, exist_ok=True)

json_pths = glob.glob(out_dir + "/*.json")

for json_pth in json_pths:
    f1 = open(json_pth, "r")
    json_data = json.load(f1)

    img_pth = os.path.join(out_dir, json_pth.replace("json", "jpg"))
    print(img_pth)
    img = cv2.imread(img_pth)
    h, w = img.shape[:2]

    tag = os.path.basename(json_pth)
    out_file = open(os.path.join(txt_dir, tag.replace("json", "txt")), "w", encoding='gbk')

    label_infos = json_data["shapes"]
    for label_info in label_infos:
        label = label_info["label"]
        points = label_info["points"]

        if len(points) < 2:
            continue

        points = np.array(points)
        xmin, xmax = max(0, min(np.unique(points[:, 0]))), min(w, max(np.unique(points[:, 0])))
        ymin, ymax = max(0, min(np.unique(points[:, 1]))), min(h, max(np.unique(points[:, 1])))

        bbox = [xmin, xmax, ymin, ymax]
        bbox_ = convert((w, h), bbox)
        cls_id = class_names.index(label)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bbox_]) + '\n')

    out_file.close()  # 关闭当前图像的标签文件
