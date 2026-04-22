import os

base = "E:/application/book/one/第一卷（裂土求生）"
new_folder = "05-第五部分（卷末）"

path = os.path.join(base, new_folder)
if not os.path.exists(path):
    os.makedirs(path)
    print(f"Created: {new_folder}")
else:
    print(f"Already exists: {new_folder}")

print("\nCurrent folders:")
for f in sorted(os.listdir(base)):
    print(f"  {f}")