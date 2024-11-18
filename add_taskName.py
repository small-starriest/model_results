import os
import json

current_dir = '.'

for dir_name in os.listdir(current_dir):
    dir_path = os.path.join(current_dir, dir_name)
    external_path = os.path.join(dir_path, "external")

    # 确保 'external' 目录存在
    if os.path.isdir(external_path):
        for file_name in os.listdir(external_path):
            file_path = os.path.join(external_path, file_name)

            # 只处理 JSON 文件
            if file_name.endswith('.json'):
                # 读取 JSON 文件
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)

                # 假设 x 的值在 data["queries"]["NDCG@10"] 中
                if "queries" not in data and "NDCG@10" in data["queries"]:
                    x = data["queries"]["NDCG@10"]

                    # 增加 "task_name" 字段
                    data["task_name"] = file_name

                    # 添加 "scores" 字段
                    data["scores"] = {
                        "test": [
                            {
                                "hf_subset": "default",
                                "NDCG@10": x,
                                                            }
                        ]
                    }

                    # 将修改后的数据写回文件
                    with open(file_path, 'w', encoding='utf-8') as f:
                        json.dump(data, f, ensure_ascii=False, indent=4)

                else:
                    print(f"Warning: 'NDCG@10' not found in 'queries' for file: {file_path}")