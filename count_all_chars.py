import os
import glob

# 统计所有章节
all_files = glob.glob('第一卷（裂土求生）/**/*.txt', recursive=True)
all_files.sort(key=lambda x: int(os.path.basename(x).split('第')[1].split('章')[0]))

total_chars = 0
print("=" * 50)
print("章节字数统计")
print("=" * 50)

for f in all_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
        # 去掉章节末尾的【本章要点】部分计算正文字数
        if '---' in content:
            body = content.split('---')[0]
        else:
            body = content
        chars = len(body.strip())
        total_chars += chars
        name = os.path.basename(f)
        # 获取章节号
        chapter_num = name.split('第')[1].split('章')[0]
        print(f'第{chapter_num}章: {chars} 字')

print("=" * 50)
print(f'已写章数: {len(all_files)} 章')
print(f'总字数: {total_chars} 字')
print(f'平均每章: {total_chars // len(all_files)} 字')
print("=" * 50)

# 检查各部分字数
parts = {}
for f in all_files:
    part = os.path.dirname(f).split(os.sep)[-1]
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
        if '---' in content:
            body = content.split('---')[0]
        else:
            body = content
        chars = len(body.strip())
        parts[part] = parts.get(part, 0) + chars

print("\n各部分字数:")
for part, chars in parts.items():
    print(f'  {part}: {chars} 字')