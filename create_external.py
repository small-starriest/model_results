import os
import shutil  # 用于移动文件


def create_external_folders_for_files():
    # 获取当前目录
    current_directory = os.getcwd()

    # 遍历当前目录下的所有文件和文件夹
    for item in os.listdir(current_directory):
        item_path = os.path.join(current_directory, item)

        # 确保是文件夹（不是其他文件）
        if os.path.isdir(item_path):
            # 定义 external 文件夹路径
            external_folder_path = os.path.join(item_path, "external")

            # 检查 external 文件夹是否已存在
            if not os.path.exists(external_folder_path):
                os.mkdir(external_folder_path)  # 创建 external 文件夹
                print(f"Created 'external' folder for directory: {item}")

                # 遍历原文件夹中的所有文件
                for file in os.listdir(item_path):
                    file_path = os.path.join(item_path, file)

                    # 确保是文件
                    if os.path.isfile(file_path):
                        # 移动文件到 external 文件夹
                        shutil.move(file_path, external_folder_path)
                        print(f"Moved file: {file} to 'external' folder")
            else:
                print(f"'external' folder already exists for: {item}")
        else:
            print(f"Skipping non-directory item: {item}")


if __name__ == "__main__":
    create_external_folders_for_files()