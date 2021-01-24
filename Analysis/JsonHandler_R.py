import json
import os.path
from Analysis.Detail_info import getRouteInfo, SearchTarget
from WebTask.Web_Crawler import Download_Task

def LoadDetail(Region, RouteName):
    #搜尋路線(站序)---線性搜尋
    RouteDetail = {}
    with open(f"./RouteMap/{Region}_RouteMap.json", 'r') as f:
        RouteDetail = json.loads(f.read())
    Output = []
    for Run in RouteDetail:
        if(Run['RouteName']['Zh_tw'] == RouteName):
            Output.append(Run)
    return Output

def getRouteDetail(RouteName):
    #取得站序
    Output = []
    Map = LoadDetail("TPE", RouteName)
    if(Map == []):
        Map = LoadDetail("NWT", RouteName)

    #取得各站動態
    URL = f"https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/Taipei/{RouteName}?$orderby=StopID&$format=JSON"
    Output_Code, StationTime = Download_Task(URL)
    if(StationTime == "[]"):
        URL = f"https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/NewTaipei/{RouteName}?$orderby=StopID&$format=JSON"
        Output_Code, StationTime = Download_Task(URL)
    print(Output_Code)
    #取得車輛動態
    URL = f"https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeNearStop/City/Taipei/{RouteName}?$orderby=StopID&$format=JSON"
    Output_Code, BusTime = Download_Task(URL)
    if(BusTime == "[]"):
        URL = f"https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeNearStop/City/NewTaipei/{RouteName}?$orderby=StopID&$format=JSON"
        Output_Code, BusTime = Download_Task(URL)
    print(Output_Code)

    #動態資料整理
    for Run in Map:
        Output.append(Analysis_StationMoving(Run, json.loads(StationTime), json.loads(BusTime)))

    return Output


def Analysis_StationMoving(RouteMap, StationTime, BusTime):
    Output = ""

    RouteUID = RouteMap["RouteUID"]
    RouteInfo = getRouteInfo(RouteUID)
    Direction = RouteMap["Direction"]

    Output += RouteInfo["RouteName"]["Zh_tw"] + "\n"
    if(Direction == 0):
        Output += f"往{RouteInfo['DestinationStopNameZh']}\n\n"
    else:
        Output += f"往{RouteInfo['DepartureStopNameZh']}\n\n"
    
    for StopInfo in RouteMap["Stops"]:
        StopID = StopInfo["StopID"]
        EstimatedTime = SearchTarget(StopID, StationTime, 1)
        BusNum = SearchTarget(StopID, BusTime, 1)
        CarNum = ""
        if(BusNum != None):
            CarNum = f"[{BusNum['PlateNumb']}]"
        Output += f"{AnalysisStopStatus(EstimatedTime)}\t{StopInfo['StopName']['Zh_tw']}\t\t{CarNum}\n"

    return Output

def AnalysisStopStatus(Item):
    Output = ""
    if(Item["StopStatus"] == 0):
        Mins = Item["EstimateTime"] // 60
        if(Mins < 2):
            Output = "即將進站"
        else:    
            Output = str(Mins) + "分鐘"
    elif(Item["StopStatus"] == 1):
        try:
            Output = str(Item["EstimateTime"] // 60) + "分鐘"
        except:
            Output = "目前未發車"                
    elif(Item["StopStatus"] == 2):
        Output = "交管不停靠"
    elif(Item["StopStatus"] == 3):
        Output = "末班車已過"
    elif(Item["StopStatus"] == 4):
        Output = "今日未營運"
    return Output