from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 创建 Chrome WebDriver 实例
driver = webdriver.Edge()

# 打开百度首页
driver.get("https://www.baidu.com")

# 查找搜索框元素
search_box = driver.find_element(By.XPATH,r'//*[@id="chat-textarea"]')

# 在搜索框中输入 "Runoob"
search_box.send_keys("Runoob")

# 模拟按下回车键
search_box.send_keys(Keys.RETURN)

time.sleep(50)  # 等待几秒钟以便查看结果
# 关闭浏览器
driver.quit()