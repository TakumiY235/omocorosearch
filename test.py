import time  # スリープを使うために必要
from selenium import webdriver  # Webブラウザを自動操作する（python -m pip install selenium)
import chromedriver_binary

driver = webdriver.Chrome()  # Chromeを準備
driver.get('https://www.google.com/')  # Googleを開く

search = driver.find_element_by_name('q')
search.send_keys('オモコロ')
search.submit()
time.sleep(5)  # 5秒間待機
driver.quit()  # ブラウザを閉じる
