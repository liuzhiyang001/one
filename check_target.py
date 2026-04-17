import os
import glob

all_files = glob.glob('第一卷（裂土求生）/**/*.txt', recursive=True)
all_files.sort(key=lambda x: int(os.path.basename(x).split('第')[1].split('章')[0]))

total_chars = 0
达标 = 0
未达标 = 0
偏少 = []
偏多 = []

print("=" * 60)
print("章节字数达标检查 (目标: 2000-2500字)")
print("=" * 60)

for f in all_files:
    with open(f, 'r', encoding='utf-8') as fp:
        content = fp.read()
        if '---' in content:
            body = content.split('---')[0]
        else:
            body = content
        chars = len(body.strip())
        total_chars += chars
        name = os.path.basename(f).replace('.txt', '')
        chapter_num = int(name.split('第')[1].split('章')[0])

        if 2000 <= chars <= 2500:
            status = "[OK]"
            达标 += 1
        elif chars < 2000:
            status = "[少]"
            未达标 += 1
            偏少.append((chapter_num, chars))
        else:
            status = "[多]"
            未达标 += 1
            偏多.append((chapter_num, chars))

        print(f'{name}: {chars}字 {status}')

print("=" * 60)
print(f'总章数: {len(all_files)}章')
print(f'总字数: {total_chars}字')
print(f'平均每章: {total_chars // len(all_files)}字')
print("-" * 60)
print(f'达标(2000-2500): {达标}章 ({达标*100//len(all_files)}%)')
print(f'偏少(<2000): {len(偏少)}章')
print(f'偏多(>2500): {len(偏多)}章')
print("=" * 60)

if 偏少:
    print("\n偏少章节 (需补充):")
    for num, chars in sorted(偏少):
        print(f'  第{num}章: {chars}字 (差{2000-chars}字)')

if 偏多:
    print("\n偏多章节 (可精简):")
    for num, chars in sorted(偏多):
        print(f'  第{num}章: {chars}字 (多{chars-2500}字)')