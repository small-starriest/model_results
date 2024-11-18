import os
import shutil

# 当前目录
current_dir = '.'

# 遍历当前目录下的所有文件和目录
for dir_name in os.listdir(current_dir):
    dir_path = os.path.join(current_dir, dir_name)

    if os.path.isdir(dir_path):  # 仅处理目录
        # 检查当前目录下是否有 'default' 子文件夹
        default_dir_path = os.path.join(dir_path, '7d24eac886a6ae6653a6b67433e1c302cb0e9ac6')

        if os.path.isdir(default_dir_path):  # 如果存在 'default' 文件夹
            # 删除 'default' 文件夹
            shutil.rmtree(default_dir_path)
            print(f"Deleted '7d24eac886a6ae6653a6b67433e1c302cb0e9ac6' folder in {dir_path}")