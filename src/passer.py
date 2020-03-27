from selenium import webdriver
from time import sleep

from test import get_data




class GoogleForm():
    def __init__(self, url, mail, pw):
        self.url = "https://drive.google.com/drive/u/0/my-drive"
        self.form = url
        self.mail = mail
        self.pw = pw


    def paste_shit(self):
        """
        This stuf execute the browser window
        """
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("start-maximized") # open Browser in maximized mode
        self.options.add_argument("disable-infobars") # disabling infobars
        self.options.add_argument("--disable-extensions") # disabling extensions
        self.options.add_argument("--disable-dev-shm-usage") # overcome limited resource problems
        self.options.add_argument("--no-sandbox") # Bypass OS security model
        self.driver = webdriver.Chrome(executable_path = "/usr/local/bin/chromedriver", options = self.options)
        self.driver.get(self.url)

        self.driver.find_element_by_xpath("//*[@id=\"identifierId\"]")\
                    .send_keys(self.mail)
        self.driver.find_element_by_xpath("//*[@id=\"identifierNext\"]/span/span")\
                    .click()
        sleep(2)
        self.driver.find_element_by_xpath("//*[@class=\"whsOnd zHQkBf\"]")\
                    .send_keys(self.pw)
        self.driver.find_element_by_xpath("//*[@id=\"passwordNext\"]/span/span")\
                    .click()
        sleep(5)
        url  = "https://docs.google.com/forms/d/1Vu_OAVkCzTH_v4GnZah2AA9lE3GpKeux3wEwSska0w4/edit"
        self.driver.get(url)
        sleep(1)

        element = self.driver.find_element_by_xpath("//*[@id=\"SchemaEditor\"]/div/div[2]/div/div[2]/div[3]")
        all_options = element.find_elements_by_xpath("//*[@jscontroller=\"RKFxf\"]")
        """
        getting questions and answers fro, prepared txt file
        """
        questions, answers = get_data()
        
        for q, a, option in zip(questions, answers, all_options):
            option.click()
            option.send_keys(q)
            
            # text.send_keys(q)
            # value="Option 1"
            # PATH = "//input[@class=\"quantumWizTextinputSimpleinputInput exportInput\"]"
            # opt = option.find_element_by_xpath(PATH)
            # opt.click()
            # opt.send_keys("egw")
            # for ans, p in zip(a,all_points):
            #     p.click()
            #     p.send_keys(ans)

        # sleep(120)
        self.driver.quit()

if __name__ == "__main__":
    url = "https://docs.google.com/forms/d/1Vu_OAVkCzTH_v4GnZah2AA9lE3GpKeux3wEwSska0w4/edit"
    """
    To manipulate the GF script need to use your credentials
    """
    mail = "EMAIL"
    pw = "PASSWORD"
    s = GoogleForm(url, mail, pw)
    s.paste_shit()
    del s