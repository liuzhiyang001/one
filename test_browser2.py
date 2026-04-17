from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

options = Options()
# 不使用用户数据目录，避免与正在运行的 Chrome 冲突
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

print("启动浏览器...")
try:
    driver = webdriver.Chrome(options=options)
    print("浏览器启动成功")

    print("导航到上传页面...")
    driver.get("https://zuozhe.qimao.com/front/book-upload?id=11776785&title=裂星衍道")

    print("当前 URL:", driver.current_url)
    print("页面标题:", driver.title)

    # 获取页面结构
    print("\n页面 HTML 结构 (前5000字符):")
    print(driver.page_source[:5000])

    # 截图保存
    driver.save_screenshot("E:/application/book/one/page_screenshot.png")
    print("\n截图已保存到 page_screenshot.png")

    time.sleep(3)
    driver.quit()
    print("浏览器已关闭")

except Exception as e:
    print(f"错误: {e}")
    import traceback
    traceback.print_exc()