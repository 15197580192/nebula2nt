import json

# 打开 txt 文件并逐行读取 JSON 数据
with open("./input/edge.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # 逐行读取数据

nt_triples = []
for line in lines:
    # 将每行的 JSON 字符串解析为 Python 字典
    data = json.loads(line.strip())  # 去掉行末的换行符，并转换为字典

    # 提取相关信息
    v_id = data["v1"]  # 起点 ID
    v2_id = data["v2"]     # 终点 ID
    relation = data["type"]          # 边类型

    # 创建 N-Triples 语句，格式为 <起点 ID> <边类型> <终点 ID>
    nt_triples.append(f"<{v_id}> <{relation}> <{v2_id}> .")

# 将 N-Triples 语句写入 NT 文件
with open("./output/edge.nt", "w", encoding="utf-8") as nt_file:
    for triple in nt_triples:
        nt_file.write(triple + "\n")
# 写入一个总文件        
with open("./output/all.nt", "a", encoding="utf-8") as nt_file:
    for triple in nt_triples:
        nt_file.write(triple + "\n")

print("NT 文件已生成！")
