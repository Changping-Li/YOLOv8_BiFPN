import os
import shutil
import re

# 指定包含图像和标签的文件夹路径
image_folder = "G:/UAV/dataset/dataset1019/images"
label_folder = "G:/UAV/dataset/dataset1019/labels"

# 获取标签文件的文件名列表
label_files = os.listdir(label_folder)

# 定义要删除的类别
category_to_remove = "6"

# 循环处理每个标签文件
for label_file in label_files:
    if label_file.endswith(".txt"):
        # 解析标签文件名以获取图像文件名
        image_file = os.path.splitext(label_file)[0] + ".jpg"

        # 构建标签文件的完整路径
        label_file_path = os.path.join(label_folder, label_file)

        # 读取标签文件内容
        with open(label_file_path, 'r') as label_file:
            content = label_file.read()

        # 使用正则表达式查找类别标签
        category_match = re.search(r'^(\d+)\s+', content)

        if category_match:
            category = category_match.group(1)

            # 如果类别标签为要删除的类别，删除标签文件和对应的图像
            if category == category_to_remove:
                os.remove(label_file_path)  # 删除标签文件
                image_path = os.path.join(image_folder, image_file)
                if os.path.exists(image_path):
                    os.remove(image_path)  # 删除对应的图像文件
                else:
                    print(f"对应的图像文件 '{image_file}' 不存在.")

print("操作完成，已删除所有类别为6的标签及对应的图像.")
