import requests
from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
from WebTask.Encode_Text import getSign

def Download_Task(URL):
    timeNow = format_date_time(mktime(datetime.now().timetuple()))
    AppID = ""
    AppKey = ""
    Sign = getSign("x-date: " + timeNow, AppKey)

    AuthorizationText = "hmac username=\"%s\", algorithm=\"hmac-sha1\", headers=\"x-date\", signature=\"%s\"" %(AppID, Sign)
    HeaderData = {
        "Content-Type":"application/json;charset=utf-8",
        "User-Agent":"Mozilla/5.0",
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip,deflate", "Accept-Language":"en-US,en;q=0.5",
        "x-date":timeNow,
        "Authorization":AuthorizationText
    }

    Connection = requests.session()
    APIData = Connection.get(URL, headers = HeaderData)
    APIData.encoding = "UTF-8"
    Connection.close()

    return APIData.status_code, APIData.text