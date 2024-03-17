from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
import requests

url = 'https://notify-api.line.me/api/notify' #LINE API
token ='' #輸入你的 LINE notify token 

def lineNotify(token,msg): #用來發送LINE 訊息
    headers = {
        'Authorization': 'Bearer ' + token
    }
    data = {
        'message':msg
    }
    r = requests.post(url,headers=headers,data=data)

def pchomePriceTrace(productURL):
    options = Options()
    options.chrome_executable_path ="chrome-win64\chrome-win64\chrome.exe"
    driver = webdriver.Chrome(options=options) #打開瀏覽器
    driver.maximize_window() ##視窗最大
    driver.get(productURL)
    time.sleep(10) #等待10秒 完整載入網站
    firstPrice = driver.find_element(By.XPATH, "//*[contains(@class, 'o-prodPrice__price')]")
    lastPrice = firstPrice.text

    while(True):
        time.sleep(3598) #每小時檢查一次價格 3598+2 = 3600秒
        driver.get(productURL)
        time.sleep(2) #等待網站刷新
        price = driver.find_element(By.XPATH, "//*[contains(@class, 'o-prodPrice__price')]")
        if price.text != lastPrice:
            name = driver.find_element(By.XPATH,"//*[contains(@class,'o-prodMainName')]")
            lineNotify(token,"{} [最新價錢：{}]".format(name.text,price.text))
            lastPrice = price.text

################################################################################################################
