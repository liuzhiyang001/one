from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

options = Options()
# 使用用户现有的 Chrome 配置以保留登录状态
user_data = os.path.expanduser("~") + "\\AppData\\Local\\Google\\Chrome\\User Data"
options.add_argument(f"--user-data-dir={user_data}")
options.add_argument("--profile-directory=Default")

print("启动浏览器...")
driver = webdriver.Chrome(options=options)

print("导航到上传页面...")
driver.get("https://zuozhe.qimao.com/front/book-upload?id=11776785&title=裂星衍道")

print("当前 URL:", driver.current_url)
print("页面标题:", driver.title)

# 获取页面 HTML 结构
print("\n页面结构预览:")
print(driver.page_source[:3000])

print("\n等待5秒后自动关闭...")
import time
time.sleep(5)
driver.quit()
print("浏览器已关闭")