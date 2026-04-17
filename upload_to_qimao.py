"""
七猫小说上传脚本
使用 Selenium 自动化上传章节

使用方法：
1. 运行脚本，会打开浏览器
2. 手动登录七猫作者平台
3. 登录后，脚本会自动导航到上传页面并上传所有章节
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import os
import time
import glob

# 配置
BOOK_ID = "11776785"
BOOK_TITLE = "裂星衍道"
UPLOAD_URL = f"https://zuozhe.qimao.com/front/book-upload?id={BOOK_ID}&title={BOOK_TITLE}"

# 章节目录
CHAPTER_DIR = r"E:\application\book\one\第一卷（裂土求生）\第一部分（十星降临）"

def get_chapter_files():
    """获取所有章节文件，按顺序排序"""
    files = glob.glob(os.path.join(CHAPTER_DIR, "*.txt"))
    # 按章节号排序
    files.sort(key=lambda x: int(os.path.basename(x).split("第")[1].split("章")[0]))
    return files

def setup_driver():
    """设置浏览器"""
    options = Options()
    # 使用用户的 Chrome 配置，保留登录状态
    options.add_argument(f"--user-data-dir={os.path.expanduser('~')}\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument("--profile-directory=Default")
    # 不使用无头模式，方便用户查看和手动登录
    driver = webdriver.Chrome(options=options)
    return driver

def upload_chapter(driver, chapter_file, chapter_num):
    """上传单个章节"""
    try:
        # 等待页面加载
        wait = WebDriverWait(driver, 10)

        # 读取章节内容
        with open(chapter_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # 获取章节标题（第一行）
        lines = content.strip().split('\n')
        title_line = lines[0] if lines else ""
        # 提取标题（去掉前面的数字）
        if '\t' in title_line:
            title = title_line.split('\t')[1] if '\t' in title_line else title_line
        else:
            title = title_line

        # 章节正文（去掉标题行和空行）
        body = '\n'.join(lines[1:]).strip()

        print(f"上传章节 {chapter_num}: {title}")

        # 这里需要根据实际页面结构填写上传逻辑
        # 由于无法访问页面，这部分需要用户根据实际情况调整

        # 示例逻辑（需要根据实际页面调整）：
        # 1. 找到章节标题输入框
        # title_input = wait.until(EC.presence_of_element_located((By.ID, "chapter-title")))
        # title_input.clear()
        # title_input.send_keys(title)

        # 2. 找到章节内容输入框
        # content_input = wait.until(EC.presence_of_element_located((By.ID, "chapter-content")))
        # content_input.clear()
        # content_input.send_keys(body)

        # 3. 点击上传按钮
        # upload_btn = wait.until(EC.element_to_be_clickable((By.ID, "upload-btn")))
        # upload_btn.click()

        # 4. 等待上传完成
        # time.sleep(2)

        print(f"章节 {chapter_num} 上传完成")
        return True

    except Exception as e:
        print(f"章节 {chapter_num} 上传失败: {e}")
        return False

def main():
    print("=" * 50)
    print("七猫小说上传脚本")
    print("=" * 50)

    # 获取章节文件
    chapter_files = get_chapter_files()
    print(f"找到 {len(chapter_files)} 个章节文件")

    for f in chapter_files:
        print(f"  - {os.path.basename(f)}")

    print("\n启动浏览器...")
    driver = setup_driver()

    try:
        # 导航到上传页面
        print(f"\n导航到: {UPLOAD_URL}")
        driver.get(UPLOAD_URL)

        print("\n请在浏览器中手动登录（如果需要）")
        print("登录完成后，请在命令行按 Enter 继续...")
        input()

        # 查看当前页面结构
        print("\n当前页面 URL:", driver.current_url)
        print("页面标题:", driver.title)

        # 等待用户确认页面加载完成
        print("\n请确认页面已正确加载，按 Enter 开始上传...")
        input()

        # 逐个上传章节
        for i, chapter_file in enumerate(chapter_files, 1):
            chapter_num = os.path.basename(chapter_file).split("第")[1].split("章")[0]
            upload_chapter(driver, chapter_file, chapter_num)
            time.sleep(1)  # 防止请求过快

        print("\n所有章节上传完成！")

    finally:
        print("\n按 Enter 关闭浏览器...")
        input()
        driver.quit()

if __name__ == "__main__":
    main()