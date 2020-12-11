import json
import os.path

def RouteStation_List(JsonContent):
    JsonObj = json.dumps(JsonContent)

def Station_List(JsonContent):
    #取得Json內容
    JsonObj = json.loads(JsonContent)
    
    #解析經過路線
    Output = JsonObj[0]["StopName"]["Zh_tw"] + "\n"
    for Item in JsonObj:
        #取得路線資訊
        RouteInfo = getRouteInfo(Item["RouteUID"])

        Output += Item["RouteName"]["Zh_tw"] + "\t\t"
        #取得方向
        if(Item["Direction"] == 0):
            Output += "往" + RouteInfo["DestinationStopNameZh"] + "\t\t"
        elif(Item["Direction"] == 1):
            Output += "往" + RouteInfo["DepartureStopNameZh"] + "\t\t"

        if(Item["StopStatus"] == 0):
            Mins = Item["EstimateTime"] // 60
            if(Mins < 2):
                Output += "即將進站\n"
            else:    
                Output += "約" + str(Mins) + "分\n"
        elif(Item["StopStatus"] == 1):
            try:
                Output += "約" + str(Item["EstimateTime"] // 60) + "分\n"
            except:
                Output += "目前未發車\n"                
        elif(Item["StopStatus"] == 2):
            Output += "交管不停靠\n"
        elif(Item["StopStatus"] == 3):
            Output += "末班車已過\n"
        elif(Item["StopStatus"] == 4):
            Output += "今日未營運\n"
    
    return Output



def Bus_List(JsonContent):
    #取得Json內容
    JsonObj = json.loads(JsonContent)
    #取得路線資訊
    RouteUID = JsonObj[0]["RouteUID"]
    RouteInfo = getRouteInfo(RouteUID)

    Output = ""
    Output += JsonObj[0]["PlateNumb"] + "\n"
    Output += JsonObj[0]["SubRouteName"]["Zh_tw"] + "\n"
    if(JsonObj[0]["Direction"] == 0):
        Output += "往" + RouteInfo["DestinationStopNameZh"] + "\n"
    elif(JsonObj[0]["Direction"] == 1):
        Output += "往" + RouteInfo["DepartureStopNameZh"] + "\n"
    
    Output += JsonObj[0]["StopName"]["Zh_tw"]

    return Output

def getRouteInfo(RouteUID):
    #取得路線資訊檔案位置
    City = RouteUID[0:3] #取得主管機關
    db_Location = "./RouteInfo/%s_Route.json" %City

    with open(db_Location, 'r') as f:
        JsonObj = json.loads(f.read())
    
    Output = {}

    for Item in JsonObj:
        if(Item['RouteUID'] == RouteUID):
            Output = Item
            break
    
    return Output