import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
import time

url = 'https://notify-api.line.me/api/notify'  # LINE API
token = ''  # Enter your LINE notify token here / 輸入你的 LINE notify token 
logfile = './price_tracking.log'

def lineNotify(token, msg): #用來發送LINE 訊息
    headers = {'Authorization': 'Bearer ' + token}
    data = {'message': msg}
    r = requests.post(url, headers=headers, data=data)

def extractPrice(price_string):
    # Split the price string at '\n' and take the first part
    target_price_str = price_string.split('\n')[0]
    # Remove the currency symbol and comma, then convert to integer
    target_price = int(target_price_str.replace('$', '').replace(',', ''))
    return target_price

def logPriceChange(product_name, price):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"Price change for {product_name} at {timestamp}: {price}"
    logging.info(log_message)
    # print(log_message)

def pchomePriceTrace(productURL, threshold=None):
    logging.basicConfig(filename=logfile, level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(productURL)
    time.sleep(10)  # Wait for the page to load completely
    last_price = None

    while True:
        driver.get(productURL)
        time.sleep(2)  # Wait for the page to refresh
        price_element = driver.find_element(By.XPATH, "//*[contains(@class, 'o-prodPrice__price')]")
        price_str = price_element.text
        price = extractPrice(price_str)

        if price != last_price and price <= threshold:
            name_element = driver.find_element(By.XPATH, "//*[contains(@class,'o-prodMainName')]")
            product_name = name_element.text
            lineNotify(token, f"{product_name} [最新價錢：{price}]")
            logPriceChange(product_name, price)
            last_price = price
                    
        time.sleep(3598) #每小時檢查一次價格 3598+2 = 3600秒

# Original code
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time 
# import requests

# url = 'https://notify-api.line.me/api/notify' #LINE API
# token ='' #輸入你的 LINE notify token 

# def lineNotify(token,msg): #用來發送LINE 訊息
#     headers = {
#         'Authorization': 'Bearer ' + token
#     }
#     data = {
#         'message':msg
#     }
#     r = requests.post(url,headers=headers,data=data)

# def pchomePriceTrace(productURL):
#     options = Options()
#     options.chrome_executable_path ="chrome-win64\chrome-win64\chrome.exe"
#     driver = webdriver.Chrome(options=options) #打開瀏覽器
#     driver.maximize_window() ##視窗最大
#     driver.get(productURL)
#     time.sleep(10) #等待10秒 完整載入網站
#     firstPrice = driver.find_element(By.XPATH, "//*[contains(@class, 'o-prodPrice__price')]")
#     lastPrice = firstPrice.text

#     while(True):
#         time.sleep(3598) #每小時檢查一次價格 3598+2 = 3600秒
#         driver.get(productURL)
#         time.sleep(2) #等待網站刷新
#         price = driver.find_element(By.XPATH, "//*[contains(@class, 'o-prodPrice__price')]")
#         if price.text != lastPrice:
#             name = driver.find_element(By.XPATH,"//*[contains(@class,'o-prodMainName')]")
#             lineNotify(token,"{} [最新價錢：{}]".format(name.text,price.text))
#             lastPrice = price.text

# ################################################################################################################