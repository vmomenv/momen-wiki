import json

# 读取旧数据集
input_file = 'DISC-Law-SFT-Triplet-released.jsonl'
output_file = 'formatted_DISC_Law_SFT_Triplet.jsonl'

# 用于存储格式化后的数据
formatted_data = []

# 读取旧数据集并格式化
try:
    with open(input_file, 'r', encoding='utf-8') as infile:
        print(f"正在读取文件: {input_file}")
        for line_num, line in enumerate(infile, 1):
            try:
                # 解析每一行 JSON 数据
                data = json.loads(line.strip())
                
                # 提取必要信息并格式化为 Alpaca 格式
                formatted_entry = {
                    "instruction": "基于下列案件，推测可能的判决结果。",
                    "input": data.get("input", ""),
                    "output": data.get("output", "")
                }

                # 将格式化后的数据添加到列表中
                formatted_data.append(formatted_entry)
            except json.JSONDecodeError as e:
                print(f"第 {line_num} 行解析失败: {e}")
except FileNotFoundError:
    print(f"未找到文件: {input_file}")

# 确保有数据被处理后再写入文件
if formatted_data:
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for entry in formatted_data:
            outfile.write(json.dumps(entry, ensure_ascii=False) + '\n')

    print(f"数据已成功格式化并保存为 {output_file}")
else:
    print("没有数据被格式化")
