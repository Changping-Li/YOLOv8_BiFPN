# import os
#
# image_folder = 'G:/UAV/dataset/dataset1024/kite'  # 图像文件夹路径
# prefix = 'kite100244_'
#
# # 获取图像文件夹中的文件列表
# image_files = os.listdir(image_folder)
#
# # 遍历图像文件并重命名
# for image_file in image_files:
#     if image_file.endswith(('.jpg', '.png', '.jpeg')):  # 假设您的图像文件是这些格式
#         new_name = prefix + image_file
#         old_path = os.path.join(image_folder, image_file)
#         new_path = os.path.join(image_folder, new_name)
#         os.rename(old_path, new_path)

import os

# 指定文件夹路径
images_folder = 'G:/UAV/dataset/dataset1024312/images'
train_folder = 'G:/UAV/dataset/dataset1024312/train'
val_folder = 'G:/UAV/dataset/dataset1024312/val'

# 输出文件路径
train_txt_path = 'G:/UAV/dataset/dataset1024312/train.txt'
val_txt_path = 'G:/UAV/dataset/dataset1024312/val.txt'

# 获取train文件夹中的图像路径
train_image_paths = [os.path.join(images_folder, filename) for filename in os.listdir(train_folder)]

# 获取val文件夹中的图像路径
val_image_paths = [os.path.join(images_folder, filename) for filename in os.listdir(val_folder)]

# 写入train.txt文件
with open(train_txt_path, 'w') as train_file:
    train_file.write('\n'.join(train_image_paths))

# 写入val.txt文件
with open(val_txt_path, 'w') as val_file:
    val_file.write('\n'.join(val_image_paths))

print(f"{train_txt_path} and {val_txt_path} generated successfully.")

