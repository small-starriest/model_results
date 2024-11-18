import os
for dir_name in os.listdir('.'):
    if '__' in dir_name:
        dir_name = dir_name.split('__', 1)[1]
    # 删除-instruct和+instruct
    dir_name = dir_name.replace('-instruct', '').replace('+instruct', '')
    print(dir_name)