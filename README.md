# PChome 價格追蹤工具
## 功能簡介  
* **價格追蹤**：使用 Selenium 自動追蹤價格
* **價格變動通知**：一旦價格發生變化，即透過 LINE Notify 傳送 LINE 通知  
  ![method](https://raw.githubusercontent.com/HUAN-LUN/PChome-/main/result/3.png)
* **簡易GUI介面**：使用tkinter撰寫簡易GUI介面 供使用者輸入商品網址以便追蹤  
  ![method](https://raw.githubusercontent.com/HUAN-LUN/PChome-/main/result/1.png)  
  若網址正確則提示開始追蹤訊息，若網址錯誤則提示輸入PChome網址  
  ![method](https://raw.githubusercontent.com/HUAN-LUN/PChome-/main/result/2.png)  
  ![method](https://raw.githubusercontent.com/HUAN-LUN/PChome-/main/result/4.png)    
* 使用多執行緒 (threading)防止GUI視窗卡死
