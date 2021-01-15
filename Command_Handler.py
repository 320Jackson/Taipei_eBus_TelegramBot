from WebTask.Web_Crawler import Download_Task
from Analysis.JsonHandler_Sta import Station_List
from Analysis.JsonHandler_Bus import Bus_List
from Analysis.JsonHandler_R import getRouteDetail

def eBusCommand(CommandArr):
    Command = CommandArr[0]
    KeyWord = CommandArr[1]
    KeyWord = KeyWord.replace('（','(')
    KeyWord = KeyWord.replace('）',')')

    if(Command == "/route" or Command == "/route@NHITC_Bot"):
        #是否搜尋方向
        Direction = 2
        if(len(CommandArr) == 3):
            Direction = int(CommandArr[2])
        
        Buffer = getRouteDetail(KeyWord)
        Output = []

        if(Direction != 2):
            Output.append(Buffer[Direction])
        else:
            Output = Buffer        
        
        return Output

    if(Command == "/station" or Command == "/station@NHITC_Bot"):
        #是否同時搜尋路線
        RouteName = ""
        if(len(CommandArr) == 3):
            RouteName = "/" + CommandArr[2]

        Output = {}
        #搜尋臺北市各站到站資訊
        Search_URL = f"https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/Taipei{RouteName}?$format=JSON&$filter=StopName/Zh_tw eq '{KeyWord}'&$orderby=RouteUID"
        Output_Code, Buffer = Download_Task(Search_URL)
        print(Output_Code, end = "\n")
        if(Buffer != "[]"):
            Output = Station_List(Buffer, Output)

        #搜尋新北市各站到站資訊
        Search_URL = f"https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/NewTaipei{RouteName}?$format=JSON&$filter=StopName/Zh_tw eq '{KeyWord}'&$orderby=RouteUID"
        Output_Code, Buffer = Download_Task(Search_URL)
        print(Output_Code, end = "\n")
        if(Buffer != "[]"):
            Output = Station_List(Buffer, Output)
        
        strOutput = f"{KeyWord}\n"
        for Run in Output.keys():
            strOutput += f"{Run}\n{Output[Run]}\n"
        if(strOutput == ""):
            strOutput = "Station not found"

        return strOutput

    
    if(Command == "/bus" or Command == "/bus@NHITC_Bot"):
        #取得臺北市公車資料
        Search_URL = "https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeNearStop/City/Taipei?$format=JSON&$filter=PlateNumb eq '%s'" %KeyWord
        Output_Code, Output = Download_Task(Search_URL)
        print(Output_Code, end = "\n")
        
        #取得新北市公車資料
        if(Output == "[]"):
            Search_URL = "https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeNearStop/City/NewTaipei?$format=JSON&$filter=PlateNumb eq '%s'" %KeyWord
            Output_Code, Output = Download_Task(Search_URL)
            print(Output_Code, end = "\n")

        #判斷是否有找到此車輛
        if(Output == "[]"):
            Output = "Bus not found"
        else:
            Output = Bus_List(Output)
        
        return Output
