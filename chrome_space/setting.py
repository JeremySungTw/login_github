from selenium import webdriver


class driv_option(webdriver.ChromeOptions):
    def __init__(self):
        super().__init__()
        # self.add_argument('headless')
        # self.add_argument("--incognito")
        # self.add_argument('--auto-open-devtools-for-tabs') # 開發者工具
        self.add_argument('--no-sandbox')  # Linux 必要
        self.add_argument('--disable-infobars')  # 不顯示受到自动测试软件的控制

    def get_chrome_path(self):
        import os
        Dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chromedriver.exe')
        if os.path.exists(Dir):
            # print(f'*chromedriver已找到 :{Dir}')
            return Dir
        else:
            print(f'*尚未找到{os.path.dirname(os.path.abspath(__file__))}')


if __name__ == '__main__':
    set = driv_option()
    driver = webdriver.Chrome(set.get_chrome_path(), options=set)
    driver.quit()