Analysis
===
Detail_info.py
---
        Get local data, and search target.
        取得本地端資料並搜尋目標資訊

---
JsonHandler_Bus.py
---
        Analysis api data, return bus location, route information and direction.
        分析api資訊，回傳公車位置、路線資訊及方向

---
JsonHandler_R.py
---
        This feature is still developing.
        本功能正在開發中

---
JsonHandler_Sta.py
---
        Analysis api data, return station location, route information(which is go by this station) and estimated time of arrival.
        分析api資訊，回傳站位資訊，行經路線資訊及預估進站時間

---
---

Bot_Main.py
---
        Flask and telegram bot webhook listener.
        Flask及Telegram bot webhook監聽器

---
Bot_Monitor.py
---
        Show the message which received from telegram.
        顯示接受到的訊息

---
Command_Handler.py
---
        Analysis command and return different message.
        分析指令，回傳不同訊息

---

WebTask
===
Encode_Text.py
---
        Generate header with api key.
        利用API key產生Header

---
Web_Crawler.py
---
        Connect to api, and get data.
        介接API，取得資料

---

Local Data
===
RouteInfo
---
        Bus routes infomation.
        公車路線資訊

---
RouteMap
---
        Bus stops order.
        公車路線站序

---
StationInfo
---
        Stations information.
        各個站牌資訊

---
StopInfo
---
        Stops information.
        站牌資訊

---

Source
===
        Data from: Public transport data exchange
        資料來源: 交通部公共運輸整合資訊流通服務平台(PTX)

---
![image](https://ptx.transportdata.tw/PTX/logo.png)