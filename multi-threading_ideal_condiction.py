from selenium import webdriver
from bs4 import BeautifulSoup
import time
import threading 

def update():
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    driver = webdriver.Firefox(options=options)
    driver.get("https://www.amazon.in/dp/B094NRY9CK")
    soup= BeautifulSoup(driver.page_source ,'html.parser')
    driver.quit()

t_list = []
a1=time.time()
for k in range(0,15):
    t1 =threading.Thread(target=update, args=[] )
    t_list.append(t1)                    
    t1.start()

if len(t_list):
    for t_ in t_list:
        t_.join()

print("time taken to complet task in second",round(time.time() - a1))
