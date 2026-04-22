import os
import glob

base = "E:/application/book/one/第一卷（裂土求生）/05-第五部分（卷末）"
files = glob.glob(os.path.join(base, "*.txt"))

print(f"已完成章数: {len(files)}")
print("\n章节列表:")
for f in sorted(files):
    name = os.path.basename(f)
    print(f"  {name}")

# 检查缺失章节
chapters = set()
for f in files:
    name = os.path.basename(f)
    # 提取章节号
    if "第" in name and "章" in name:
        try:
            num = int(name.split("第")[1].split("章")[0])
            chapters.add(num)
        except:
            pass

print("\n缺失章节:")
for i in range(101, 126):
    if i not in chapters:
        print(f"  第{i}章")