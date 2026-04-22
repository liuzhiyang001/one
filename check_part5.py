import os
import glob

base = "E:/application/book/one/第一卷（裂土求生）/05-第五部分（卷末）"

print("Checking Part 5 folder:")
if os.path.exists(base):
    files = glob.glob(os.path.join(base, "*.txt"))
    print(f"Found {len(files)} files:")
    for f in sorted(files):
        name = os.path.basename(f)
        with open(f, 'r', encoding='utf-8') as fp:
            content = fp.read()
            # Count words
            if '---' in content and '【本章要点】' in content:
                body = content.rsplit('---', 1)[0]
            else:
                body = content
            chars = len(body.strip())
        print(f"  {name}: {chars}字")
else:
    print("Folder does not exist")