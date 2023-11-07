from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from  selenium import webdriver
from bs4 import BeautifulSoup
import time
from tkinter import *
import chromedriver_autoinstaller



chromedriver_autoinstaller.install()
url="https://www.starbucks.co.kr/store/store_map.do"

def fn_search_store():
    driver = webdriver.Edge()
    driver.implicitly_wait(3)
    driver.get(url)
    time.sleep(1)       #대기시간?

    driver.find_element(By.XPATH, '//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/header[2]/h3/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'//*[@id="container"]/div/form/fieldset/div/section/article[1]/article/article[2]/div[1]/div[2]/ul/li[5]/a').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="mCSB_2_container"]/ul/li[1]/a').click()
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    lis = soup.select('.prod_list li')

    for li in lis:
        info = li.select_one('.txt_info').text
        text.insert(END, info + '\n')

    driver.quit()



fn_search_store()
app = Tk()
app.title("STARBUCKS")
text = Text(app, width=100, height=50)
text.pack()