import json
from Analysis.Detail_info import getRouteInfo, getStopInfo

def RouteStation_List(JsonContent):
    JsonObj = json.dumps(JsonContent)

def Station_List(JsonContent, StationGroup):
    #取得Json內容
    JsonObj = json.loads(JsonContent)
    #解析經過路線
    for Item in JsonObj:
        #取得路線資訊
        RouteInfo = getRouteInfo(Item["RouteUID"])
        StopInfo = getStopInfo(Item["StopUID"])

        Output = Item["RouteName"]["Zh_tw"] + "\t\t"
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
        
        if((StopInfo["StopAddress"] in StationGroup) == False):
            StationGroup[StopInfo["StopAddress"]] = Output
        else:
            StationGroup[StopInfo["StopAddress"]] += Output

    return StationGroup