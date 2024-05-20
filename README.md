# PChome 價格追蹤工具

## 功能簡介
自動追蹤 PChome 網站商品價格，當商品價格變動時，傳送LINE訊息通知使用者並把商品價格變動記錄下來

提供 GUI 介面，方便使用者操作。

* 當價格變動時，終端機顯示通知：

  ![method](https://raw.githubusercontent.com/Baconbuilder/PChome-/main/result/5.png)

## 功能說明
* **價格追蹤**：使用 Selenium 自動追蹤價格。
* **價格變動通知**：當商品價格變動且低於設定的閾值時，會在終端機顯示通知並記錄到日誌文件中。
* **價格歷史記錄**：所有價格變動都會被記錄到日誌文件中。
* **簡易 GUI 介面**：使用 tkinter 撰寫簡易 GUI 介面供使用者輸入商品網址以便追蹤。

  ![method](https://raw.githubusercontent.com/Baconbuilder/PChome-/main/result/1.png)

  若網址正確則提示開始追蹤訊息，若網址錯誤則提示輸入 PChome 網址。

  ![method](https://raw.githubusercontent.com/Baconbuilder/PChome-/main/result/2.png)

  ![method](https://raw.githubusercontent.com/Baconbuilder/PChome-/main/result/4.png)
* **使用多執行緒 (threading)**：防止 GUI 視窗卡死。
* **日誌功能**：記錄所有價格變動，存儲在 `price_tracking.log` 中。

## 使用說明
1. clone本專案：
    ```bash
    git clone https://github.com/HUAN-LUN/PChome-.git
    ```
2. 安裝所需的 Python 套件：
    ```bash
    pip install -r requirements.txt
    ```
3. 透過 GUI 輸入商品的 PChome 網址開始追蹤價格。

## 注意
* 若要接收 LINE 通知，請將 `lineNotify` 函數啟用並輸入你的 LINE notify token。



