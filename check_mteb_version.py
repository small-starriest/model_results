import os
import json

# 当前目录
current_dir = '.'

# 遍历当前目录下的所有文件和目录
for dir_name in os.listdir(current_dir):
    dir_path = os.path.join(current_dir, dir_name)

    if os.path.isdir(dir_path):  # 仅处理目录
        # 检查目录中的所有 .json 文件
        for file_name in os.listdir(dir_path):
            if file_name.endswith('.json'):
                json_file_path = os.path.join(dir_path, file_name)

                # 尝试打开并解析 .json 文件
                try:
                    with open(json_file_path, 'r', encoding='utf-8') as json_file:
                        data = json.load(json_file)

                        # 检查 'mteb_version' 是否在 JSON 数据中
                        if 'mteb_version' not in data:
                            print(f"{json_file_path} does not contain 'mteb_version'")
                except Exception as e:
                    print(f"Error reading {json_file_path}: {e}")