# import os
# import random
#
# xmlfilepath = r'datasets/VOCTrainVal/Annotations/'  # xml文件的路径
# saveBasePath = r'datasets/VOCTrainVal/ImageSets/'  # 生成的txt文件的保存路径
#
# trainval_percent = 0.8  # 训练验证集占整个数据集的比重（划分训练集和测试验证集）
# train_percent = 0.8  # 训练集占整个训练验证集的比重（划分训练集和验证集）
# total_xml = os.listdir(xmlfilepath)
# num = len(total_xml)
# list = range(num)
# tv = int(num * trainval_percent)
# tr = int(tv * train_percent)
# trainval = random.sample(list, tv)
# train = random.sample(trainval, tr)
#
# print("train and val size", tv)
# print("traub suze", tr)
# ftrainval = open(os.path.join(saveBasePath, 'Main/trainval.txt'), 'w')
# ftest = open(os.path.join(saveBasePath, 'Main/test.txt'), 'w')
# ftrain = open(os.path.join(saveBasePath, 'Main/train.txt'), 'w')
# fval = open(os.path.join(saveBasePath, 'Main/val.txt'), 'w')
#
# for i in list:
#     name = total_xml[i][:-4] + '\n'
#     if i in trainval:
#         ftrainval.write(name)
#         if i in train:
#             ftrain.write(name)
#         else:
#             fval.write(name)
#     else:
#         ftest.write(name)
#
# ftrainval.close()
# ftrain.close()
# fval.close()
# ftest.close()



# import os

# # 指定图像文件夹路径
# image_folder = 'G:/UAV/dataset/dataset_2/images'
#
# # 指定要保存的txt文件路径
# txt_file = 'G:/UAV/code/ultralytics-8940a27bdb26895f09a1554514a9a46312aa89c3/ultralytics/yolo/v8/detect/VOCTest/test.txt'
#
# # 获取图像文件夹中的所有图像文件的路径
# image_paths = [os.path.join(image_folder, filename) for filename in os.listdir(image_folder) if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif'))]
#
# # 打开txt文件以写入模式
# with open(txt_file, 'w') as file:
#     # 将图像文件路径逐行写入txt文件
#     for image_path in image_paths:
#         file.write(image_path + '\n')
#
# print(f"Image paths have been saved to {txt_file}")



#现有两个文件夹，一个存放jpg图像及其对应的标注信息json文件。另一个文件夹包含txt格式的label文件
#现需将labels按8：2划分成训练集和验证集，同时给出两个txt,分别存放训练集和验证集的图像路径信息
import os
import random
import shutil

# 定义文件夹路径
image_folder = 'G:/UAV/dataset/dataset1024/images'
label_folder = 'G:/UAV/dataset/dataset1024/labels'
train_txt = 'G:/UAV/dataset/dataset1024/train.txt'
val_txt = 'G:/UAV/dataset/dataset1024/val.txt'

# 创建train_image和val_image文件夹
train_image_folder = 'G:/UAV/dataset/dataset1024/train_image'
val_image_folder = 'G:/UAV/dataset/dataset1024/val_image'

os.makedirs(train_image_folder, exist_ok=True)
os.makedirs(val_image_folder, exist_ok=True)

# 获取所有标签文件的文件名
label_files = os.listdir(label_folder)

# 打乱标签文件的顺序
random.shuffle(label_files)

# 计算划分的索引位置
split_index = int(0.8 * len(label_files))

# 分割训练集和验证集的标签文件
train_labels = label_files[:split_index]
val_labels = label_files[split_index:]

# 写入训练集的图像路径信息到train.txt，并将图像移到train_image文件夹
with open(train_txt, 'w') as f_train:
    for label_file in train_labels:
        image_file = label_file.replace('.txt', '.jpg')
        image_path = os.path.join(image_folder, image_file)
        f_train.write(image_path + '\n')
        shutil.copy(image_path, os.path.join(train_image_folder, image_file))

# 写入验证集的图像路径信息到val.txt，并将图像移到val_image文件夹
with open(val_txt, 'w') as f_val:
    for label_file in val_labels:
        image_file = label_file.replace('.txt', '.jpg')
        image_path = os.path.join(image_folder, image_file)
        f_val.write(image_path + '\n')
        shutil.copy(image_path, os.path.join(val_image_folder, image_file))

# import os
#
# # 定义图像文件夹和标签文件夹的路径
# images_folder = 'G:/UAV\dataset/dataset_2/images'
# labels_folder = 'G:/UAV\dataset/dataset_2/labels'
#
# # 获取图像文件夹和标签文件夹中的文件列表
# image_files = os.listdir(images_folder)
# label_files = os.listdir(labels_folder)
#
# # 提取标签名称，假设图像和标签的文件名都是相同的
# image_labels = [os.path.splitext(file)[0] for file in image_files]
# label_labels = [os.path.splitext(file)[0] for file in label_files]
#
# # 找出labels文件夹下多余的标签
# extra_labels = list(set(image_labels) - set(label_labels))
#
# # 打印多余的标签
# if extra_labels:
#     print("以下标签在labels文件夹中存在，但在images文件夹中不存在：")
#     for label in extra_labels:
#         print(label)
# else:
#     print("labels文件夹中没有多余的标签。")



#现有两个文件夹，一个存放jpg图像及其对应的标注信息json文件。另一个文件夹包含txt格式的label文件
#现需将labels按8：2划分成训练集和验证集，同时给出两个txt,分别存放训练集和验证集的图像路径信息
# import os
# import random
#
# # 设置文件夹路径
# image_folder = 'G:/UAV/dataset/dataset_2/images'
# label_folder = 'G:/UAV/dataset/dataset_2/labels'
#
# # 读取图像文件列表
# image_files = os.listdir(image_folder)
# image_files = [f for f in image_files if f.endswith('.jpg')]
#
# # 创建训练集和验证集的文件
# train_file = open('G:/UAV/dataset/dataset_2/train.txt', 'w')
# val_file = open('G:/UAV/dataset/dataset_2/val.txt', 'w')
#
# # 创建类别字典，用于存储每个类别的图像路径列表
# class_to_images = {}
#
# # 遍历图像文件
# for image_filename in image_files:
#     # 提取类别信息
#     label_filename = os.path.splitext(image_filename)[0] + '.txt'
#     label_path = os.path.join(label_folder, label_filename)
#
#     with open(label_path, 'r') as f:
#         first_line = f.readline()
#         class_name = first_line.strip().split()[0]  # 假设第一个数字表示类别
#
#     # 如果类别不在字典中，则创建一个新的列表
#     if class_name not in class_to_images:
#         class_to_images[class_name] = []
#
#     # 将图像路径添加到相应类别的列表中
#     class_to_images[class_name].append(os.path.join(image_folder, image_filename))
#
# # 遍历每个类别，将图像分配到训练集和验证集
# for class_name, images in class_to_images.items():
#     num_images = len(images)
#     num_train = int(0.8 * num_images)
#     num_val = num_images - num_train
#
#     # 随机打乱图像列表
#     random.shuffle(images)
#
#     # 分配到训练集
#     for image_path in images[:num_train]:
#         train_file.write(image_path + '\n')
#
#     # 分配到验证集
#     for image_path in images[num_train:]:
#         val_file.write(image_path + '\n')
#
# # 关闭文件
# train_file.close()
# val_file.close()

#现有一个文件夹，里面有很多txt的文本，现在遍历每个txt的文本的每一行，每行内容包含用空格隔开多个数字，若该行开头数字为5则删除该行，如果删除后该txt为空，则直接删除该txt。使用python实现。另外，若删除txt同时也要删除另一个文件夹下和它同名的jpg和json文件
# import os
# import shutil
#
# # 指定要处理的txt文件所在的文件夹路径
# txt_folder_path = 'G:/UAV/dataset/dataset_2/labels'
#
# # 指定存放json和jpg文件的文件夹路径
# other_folder_path = 'G:/UAV/dataset/dataset_2/images'
#
# # 遍历txt文件夹中的所有txt文件
# for root, dirs, files in os.walk(txt_folder_path):
#     for file in files:
#         if file.endswith('.txt'):
#             txt_file_path = os.path.join(root, file)
#             jpg_file_path = os.path.join(other_folder_path, os.path.splitext(file)[0] + '.jpg')
#             json_file_path = os.path.join(other_folder_path, os.path.splitext(file)[0] + '.json')
#
#             # 用于存储过滤后的文本行
#             filtered_lines = []
#
#             # 打开txt文件并逐行处理
#             with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
#                 for line in txt_file:
#                     # 检查每行的开头数字是否为5
#                     if not line.strip().startswith('7'):
#                         filtered_lines.append(line)
#
#             # 如果文本行不为空，写回txt文件
#             if filtered_lines:
#                 with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
#                     txt_file.writelines(filtered_lines)
#             else:
#                 # 如果文本行为空，删除txt文件以及对应的jpg和json文件
#                 print(txt_file_path)
#                 os.remove(txt_file_path)
#                 if os.path.exists(jpg_file_path):
#                     os.remove(jpg_file_path)
#                 if os.path.exists(json_file_path):
#                     os.remove(json_file_path)

# import os
#
# # 指定文件夹路径
# folder_path = 'G:/UAV/dataset/dataset_2/images_2'
#
# # 遍历文件夹中的所有文件
# for filename in os.listdir(folder_path):
#     # 检查文件是否是jpg文件
#     if filename.endswith('.jpg'):
#         # 构建新的文件名，加上"ballon_"
#         new_filename = 'different_' + filename
#
#         # 构建文件的完整路径
#         old_filepath = os.path.join(folder_path, filename)
#         new_filepath = os.path.join(folder_path, new_filename)
#
#         # 重命名文件
#         os.rename(old_filepath, new_filepath)
#         print(f'Renamed {filename} to {new_filename}')
#
#     if filename.endswith('.json'):
#         # 构建新的文件名，加上"ballon_"
#         new_filename = 'different_' + filename
#
#         # 构建文件的完整路径
#         old_filepath = os.path.join(folder_path, filename)
#         new_filepath = os.path.join(folder_path, new_filename)
#
#         # 重命名文件
#         os.rename(old_filepath, new_filepath)
#         print(f'Renamed {filename} to {new_filename}')

