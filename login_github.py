from selenium import webdriver
from chrome_space import setting
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def waitweb(time_loop, css, success_msg, error_msg='找不到此元素'):
    for _ in range(time_loop):
        css_obj = driver.execute_script(css)
        if css_obj:
            print(success_msg)
            return css_obj[0]
        time.sleep(1)
    print(error_msg)


# 參數
url = 'https://github.com/login'  # 網址
username = ''  # Username or email address
password = ''  # Password

set = setting.driv_option()
driver = webdriver.Chrome(set.get_chrome_path(), options=set)
driver.set_window_size(1500, 1020)
driver.get(url)

try:
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR,"body > div.footer.container-lg.p-responsive.py-6.mt-6.f6 > ul > li:nth-child(4) > a")))  # 等待元素五秒出現
    print(f'開始登入Github，使用帳號：{username}，密碼為：{password}')
    driver.find_element_by_id('login_field').send_keys(username)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_css_selector('.btn.btn-primary.btn-block').click()
    WaitWeb(5, "return document.getElementsByClassName('flash flash-full flash-error')", '顯示帳密錯誤訊息', '查找不到帳密錯誤訊息，進行下一步')
    WaitWeb(5, "return document.getElementsByClassName('d-flex flex-column flex-lg-row flex-self-stretch flex-lg-self-auto')", '登入成功')
    driver.quit()
except:
    print('查找不到[Contact GitHub]的元素，請確認url是否為https://github.com/login')
    driver.quit()
