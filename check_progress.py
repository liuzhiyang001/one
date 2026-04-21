import os
import glob

# Check all chapter files
all_files = glob.glob('第一卷（裂土求生）/**/*.txt', recursive=True)
if all_files:
    all_files.sort(key=lambda x: int(os.path.basename(x).split('第')[1].split('章')[0]))
    print(f"已写章数: {len(all_files)}")
    print(f"最后一章: {os.path.basename(all_files[-1])}")
    for f in all_files[-5:]:
        print(f"  {os.path.basename(f)}")
else:
    print("没有找到章节文件")

# Check directory structure
parts = glob.glob('第一卷（裂土求生）/*')
print(f"\n已存在的部分目录: {len(parts)}")
for p in parts:
    print(f"  {os.path.basename(p)}")