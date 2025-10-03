import json

with open(r"C:\Users\18310\Downloads\AMQA_Dataset.jsonl", "r", encoding="utf-8") as f:
    lines = [json.loads(line) for line in f]

with open(r"C:\Users\18310\Downloads\AMQA_Dataset.jsonl", "w", encoding="utf-8") as f:
    json.dump(lines, f, indent=2, ensure_ascii=False)
