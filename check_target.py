"""
《裂星衍道》字数检查工具
检查各章节字数是否达到 2000-2500 字的目标
"""

import os
import glob
import sys

# 设置输出编码
sys.stdout.reconfigure(encoding='utf-8')

def count_words():
    all_files = glob.glob('第一卷（裂土求生）/**/*.txt', recursive=True)
    all_files.sort(key=lambda x: int(os.path.basename(x).split('第')[1].split('章')[0]))

    total_chars = 0
    ok_count = 0
    low_count = 0
    high_count = 0
    low_chapters = []
    high_chapters = []

    print("=" * 60)
    print("章节字数达标检查 (目标: 2000-2500字)")
    print("=" * 60)

    for f in all_files:
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
            # 去掉章节末尾的【本章要点】部分计算正文字数
            # 使用rsplit从右边分割，只分割一次，避免与文中场景转换分隔符冲突
            if '---' in content and '【本章要点】' in content:
                body = content.rsplit('---', 1)[0]
            else:
                body = content
            chars = len(body.strip())
            total_chars += chars
            name = os.path.basename(f).replace('.txt', '')
            chapter_num = int(name.split('第')[1].split('章')[0])

            if 2000 <= chars <= 2500:
                status = "[OK]"
                ok_count += 1
            elif chars < 2000:
                status = "[少]"
                low_count += 1
                low_chapters.append((chapter_num, chars, name))
            else:
                status = "[多]"
                high_count += 1
                high_chapters.append((chapter_num, chars, name))

            print(f'{name}: {chars}字 {status}')

    print("=" * 60)
    print(f'总章数: {len(all_files)}章')
    print(f'总字数: {total_chars}字')
    print(f'平均每章: {total_chars // len(all_files)}字')
    print("-" * 60)
    print(f'达标(2000-2500): {ok_count}章 ({ok_count*100//len(all_files)}%)')
    print(f'偏少(<2000): {low_count}章')
    print(f'偏多(>2500): {high_count}章')
    print("=" * 60)

    if low_chapters:
        print("\n偏少章节 (需补充):")
        for num, chars, name in sorted(low_chapters):
            diff = 2000 - chars
            print(f'  第{num}章 [{name}]: {chars}字 (差{diff}字)')

    if high_chapters:
        print("\n偏多章节 (可精简):")
        for num, chars, name in sorted(high_chapters):
            diff = chars - 2500
            print(f'  第{num}章 [{name}]: {chars}字 (多{diff}字)')

    return ok_count, low_count, high_count

if __name__ == "__main__":
    count_words()