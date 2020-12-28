import json
from Analysis.Detail_info import getRouteInfo

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
    print(Output)

    return Output