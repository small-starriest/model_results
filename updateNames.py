import os

def rename_directories():
    # 获取当前目录下的所有目录和文件
    for dir_name in os.listdir('.'):
        if os.path.isdir(dir_name):  # 仅处理目录
            new_name = dir_name  # 初始化新名称为原目录名

            # 如果目录名包含 "-instruct"，则删除它
            if '+instruct' in dir_name:
                new_name = dir_name.replace('+instruct', '-instruct')
                print("update " + new_name)



            # 如果目录名有变化，重命名目录
            if new_name != dir_name:
                print(f"Renaming: {dir_name} -> {new_name}")
                os.rename(dir_name, new_name)

# 调用函数
rename_directories()
