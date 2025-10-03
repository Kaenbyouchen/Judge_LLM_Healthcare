import json
import pandas as pd

# 1. 读取 jsonl 文件
with open(r"D:\USC Research Ruishan Liu\LLM\healthbench-data-052025\2025-05-07-06-14-12_oss_eval.jsonl", "r", encoding="utf-8") as f:
    lines = [json.loads(line) for line in f]

# 2. 转成 DataFrame
df = pd.DataFrame(lines)

# 3. 保存为 CSV
df.to_csv("oss_eval.csv", index=False, encoding="utf-8-sig")

print("转换完成！已生成 oss_eval.csv")
