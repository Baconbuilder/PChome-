import  tkinter as tk
from tkinter import*
from PCHomePriceTrace import*
import threading


#接收輸入網址
def getURL():
    URL = product_URL.get()
    if not URL.startswith("https://24h.pchome.com"):
        response.config(text="請輸入PChome商品網址")
        return
    else:
        response.config(text="成功開始追蹤價格")
        threading.Thread(target=pchomePriceTrace, args=(URL,),daemon=True).start() #用threaing持續追蹤，避免視窗卡住無回應
    



#################################################################################################

root = tk.Tk() #建立主視窗

#設定視窗名稱
root.title("PChome 價格追蹤")

#設定視窗大小
root.geometry("500x300+500+200")#寬*高 +用來固定視窗開啟後出現在螢幕上的位子

#設定視窗最小值
root.minsize(width=300,height=150)

#root.iconbitmap("爬蟲作品\robot.ico") #圖示搞不好

#設定背景顏色
root.config(background="#4F4F4F")

#設定標題標籤
title_text =Label(bg="#4F4F4F",fg="white",text="PChome 價格追蹤",font="微軟正黑體 20")
title_text.pack(pady=(30,30))
#設定輸入框
product_URL_text=Label(bg='#4F4F4F',fg="white",text='輸入PChome商品網址',font="微軟正黑體 10")
product_URL_text.pack()
product_URL =Entry(width=30)
product_URL.pack(pady=(0,10))

#設定回應
response = Label(bg='#4F4F4F',fg="white",text="",font="微軟正黑體 12")
response.pack()

#設定按鈕
btn = Button(text="輸入",font="微軟正黑體 10",command=getURL) #宣告按鈕並設定文字，以及背景顏色
btn.config(width=5,height=1)
btn.pack()



    



root.mainloop() #建立常駐視窗


