import os
import shutil

base = "第一卷（裂土求生）"

# 原文件夹名
old_names = [
    "第一部分（十星降临）",
    "第二部分（觉醒之路）",
    "第三部分（结识伙伴）"
]

# 新文件夹名（带数字前缀）
new_names = [
    "01-第一部分（十星降临）",
    "02-第二部分（觉醒之路）",
    "03-第三部分（结识伙伴）"
]

for old, new in zip(old_names, new_names):
    old_path = os.path.join(base, old)
    new_path = os.path.join(base, new)
    if os.path.exists(old_path):
        shutil.move(old_path, new_path)
        print(f"重命名: {old} -> {new}")
    else:
        print(f"文件夹不存在: {old}")

print("\n完成！新的文件夹顺序:")
for f in sorted(os.listdir(base)):
    print(f"  {f}")