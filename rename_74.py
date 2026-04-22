import os
import shutil

# 重命名第74章
base = "E:/application/book/one/第一卷（裂土求生）/03-第三部分（结识伙伴）"
old_74 = os.path.join(base, "第74章 凡境巅峰巩固.txt")
new_74 = os.path.join(base, "第74章 灵境巅峰巩固.txt")
if os.path.exists(old_74):
    shutil.move(old_74, new_74)
    print(f"重命名: 第74章 凡境巅峰巩固.txt → 第74章 灵境巅峰巩固.txt")
else:
    print(f"文件不存在: {old_74}")

print("\n当前文件列表:")
for f in sorted(os.listdir(base)):
    if f.endswith('.txt'):
        print(f"  {f}")