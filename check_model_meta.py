import os
current_dir='.'
for dir_name in os.listdir(current_dir):
    dir_path = os.path.join(current_dir, dir_name)
    dir_path = os.path.join(dir_path, "external")
    if os.path.exists(dir_path):
        for dir_name_file in os.listdir(dir_path):
            dir_name_file_meta = os.path.join(dir_path, "model.meta.json")
            if not os.path.exists(dir_name_file_meta):
                print(dir_name)
                break