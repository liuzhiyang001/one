import shutil
import os

old_folder = "E:/application/book/one/第一卷"
if os.path.exists(old_folder):
    shutil.rmtree(old_folder)
    print(f"已删除: {old_folder}")
else:
    print(f"文件夹不存在: {old_folder}")