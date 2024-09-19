import json

# 打开 txt 文件并逐行读取 JSON 数据
with open("./input/node.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()  # 逐行读取数据

nt_triples = []
for line in lines:
    # 将每行的 JSON 字符串解析为 Python 字典
    data = json.loads(line.strip())  # 去掉行末的换行符，并转换为字典
    v_id = data["vid"]
    p_id = data["v"]["jstp_hnu.id"]
    p_name = data["v"]["jstp_hnu.name"]
    p_type = data["v"]["jstp_hnu.type"]

    # 创建 N-Triples 语句，不使用 URI 前缀
    nt_triples.append(f"<{v_id}> <type> \"{p_type}\" .")
    nt_triples.append(f"<{v_id}> <name> \"{p_name}\" .")
    nt_triples.append(f"<{v_id}> <id> \"{p_id}\" .")

# 将 N-Triples 语句写入 NT 文件
with open("./output/node.nt", "w", encoding="utf-8") as nt_file:
    for triple in nt_triples:
        nt_file.write(triple + "\n")

# 写入一个总文件        
with open("./output/all.nt", "a", encoding="utf-8") as nt_file:
    for triple in nt_triples:
        nt_file.write(triple + "\n")

print("NT 文件已生成！")
