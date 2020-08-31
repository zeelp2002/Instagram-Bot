from selenium import webdriver


class InstagramBot:
    
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('chromedriver.exe')

        self.driver.get('https://www.instagram.com/')
        


if __name__ == '__main__':
    ig_bot = InstagramBot('temp_username', 'temp_password')

    
