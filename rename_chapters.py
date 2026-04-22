import os
import shutil

base = "E:/application/book/one/第一卷（裂土求生）/05-第五部分（卷末）"

# 重命名第107章
old_107 = os.path.join(base, "第107章 灵境后期.txt")
new_107 = os.path.join(base, "第107章 地境后期.txt")
if os.path.exists(old_107):
    shutil.move(old_107, new_107)
    print(f"重命名: 第107章 灵境后期.txt → 第107章 地境后期.txt")
else:
    print(f"文件不存在: {old_107}")

# 重命名第112章
old_112 = os.path.join(base, "第112章 灵境巅峰.txt")
new_112 = os.path.join(base, "第112章 地境巅峰.txt")
if os.path.exists(old_112):
    shutil.move(old_112, new_112)
    print(f"重命名: 第112章 灵境巅峰.txt → 第112章 地境巅峰.txt")
else:
    print(f"文件不存在: {old_112}")

# 验证
print("\n当前文件列表:")
for f in sorted(os.listdir(base)):
    if f.endswith('.txt'):
        print(f"  {f}")