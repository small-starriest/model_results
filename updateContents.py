import os
import shutil

# 当前目录
current_dir = '.'

# 遍历当前目录下的所有文件和目录
for dir_name in os.listdir(current_dir):
    if os.path.isdir(dir_name):  # 仅处理目录
        target_dir = r'D:\桌面\IR\results\results'  # 目标目录

        # 标志位，判断是否找到了匹配的目录
        found = False

        for dir_name_now in os.listdir(target_dir):
            if dir_name_now == dir_name:  # 如果目标目录中有和当前目录相同的目录名
                print(f"Updating {dir_name_now}")

                # 在目标目录下定义 "external" 文件夹路径
                default_dir = os.path.join(target_dir, dir_name_now, 'external')

                # 如果文件夹不存在，则创建它
                os.makedirs(default_dir, exist_ok=True)

                # 遍历当前目录下的所有文件
                for file_name in os.listdir(dir_name):
                    # 只处理 .json 文件
                    if file_name.endswith('.json'):
                        file_path = os.path.join(dir_name, file_name)

                        # 将 .json 文件复制到 "external" 目录中
                        destination_path = os.path.join(default_dir, file_name)

                        # 使用 shutil.copy() 复制文件，如果目标文件已存在可以选择是否覆盖
                        try:
                            shutil.copy(file_path, destination_path)
                            print(f"Copied {file_name} to {default_dir}")
                        except Exception as e:
                            print(f"Failed to copy {file_name} to {default_dir}: {e}")

                # # 在匹配的目录 (dir_name_now) 中查找文件夹 c 的 model_meta.json 文件
                # for dir_name_now_next in os.listdir(target_dir):
                #     if(dir_name_now_next == "7d24eac886a6ae6653a6b67433e1c302cb0e9ac6"):
                #         continue
                #     folder_c_path = os.path.join(target_dir, dir_name_now, dir_name_now_next)
                #     model_meta_file = os.path.join(folder_c_path, 'model_meta.json')
                #
                #
                #     # 验证文件的存在并复制
                #     if os.path.exists(model_meta_file):
                #         shutil.copy(model_meta_file, default_dir)
                #         print(f"Copied model_meta.json from {folder_c_path} to {default_dir}")
                #     else:
                #         print(f"model_meta.json not found in {folder_c_path}")
                #
                #     break

                found = True
                break  # 找到匹配的目录后跳出内层循环

        # 如果没有找到相同名字的目录，则创建该目录
        if not found:
            print(f"Creating new directory for {dir_name}")
            # 在目标目录下创建 dir_name 文件夹
            new_dir_path = os.path.join(target_dir, dir_name)
            os.makedirs(new_dir_path, exist_ok=True)

            # 在该目录下创建名为 "external" 的子目录
            default_dir = os.path.join(new_dir_path, 'external')
            os.makedirs(default_dir, exist_ok=True)

            # 遍历当前目录下的所有文件
            for file_name in os.listdir(dir_name):
                # 只处理 .json 文件
                if file_name.endswith('.json'):
                    file_path = os.path.join(dir_name, file_name)
                    # 将 .json 文件复制到 "default" 目录中
                    shutil.copy(file_path, os.path.join(default_dir, file_name))