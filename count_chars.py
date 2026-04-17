import os
import glob

chapter_dir = '第一卷（裂土求生）/第一部分（十星降临）'
files = glob.glob(os.path.join(chapter_dir, '*.txt'))
files.sort(key=lambda x: int(os.path.basename(x).split('第')[1].split('章')[0]))

total_chars = 0
for f in files:
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
        print(f'{name}: {chars} 字')

print(f'\n前20章总字数: {total_chars}')