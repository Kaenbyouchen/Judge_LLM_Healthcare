#!/usr/bin/env python3
import json
import urllib.request

# 1. 下载文件
# url = "https://openaipublic.blob.core.windows.net/simple-evals/healthbench/2025-05-07-06-14-12_oss_eval.jsonl"
local_path = "2025-05-07-06-14-12_oss_eval.jsonl"
# urllib.request.urlretrieve(url, local_path)
# print(f"已下载到 {local_path}")

# 2. 预览 prompt_id, 模型名, 分数
with open(local_path, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, 1):
        rec = json.loads(line)
        pid = rec.get("prompt_id")
        comps = rec.get("completions") or {}
        for model, payload in comps.items():
            print(pid, model, payload.get("score"), sep="\t")
        if i >= 3:  # 只看前三条
            break
