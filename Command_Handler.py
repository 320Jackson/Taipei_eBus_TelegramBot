from WebTask.Web_Crawler import Download_Task
from Analysis.JsonHandler_Sta import Bus_List, Station_List
from Analysis.JsonHandler_R import Analysis_StationMoving

def eBusCommand(CommandArr):
    Command = CommandArr[0]
    KeyWord = CommandArr[1]
    KeyWord = KeyWord.replace('（','(')
    KeyWord = KeyWord.replace('）',')')

    if(Command == "/route" or Command == "/route@NHITC_Bot"):
        #去程回程
        Direction = None
        if(len(CommandArr) == 3):
            Direction = CommandArr[2]
        
        Search_URL = "https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/Taipei/%s?$format=JSON&$orderby=StopSequence"  %KeyWord
        Output_Code, Buffer = Download_Task(Search_URL)
        print(Output_Code, end = "\t")
        Search_URL = f"https://ptx.transportdata.tw/MOTC/v2/Bus/RealTimeNearStop/City/Taipei/{KeyWord}?$format=JSON"
        Output_Code, BusBuffer = Download_Task(Search_URL)
        print(Output_Code, end = "\n")

        return Analysis_StationMoving(KeyWord, Buffer, BusBuffer, Direction)

    if(Command == "/station" or Command == "/station@NHITC_Bot"):
        #是否同時搜尋路線
        RouteName = ""
        if(len(CommandArr) == 3):
            RouteName = "/" + CommandArr[2]

        Output = ""
        #搜尋臺北市各站到站資訊
        Search_URL = "https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/Taipei%s?$format=JSON&$filter=StopName/Zh_tw eq '%s'&$orderby=RouteUID" %(RouteName, KeyWord)
        Output_Code, Buffer = Download_Task(Search_URL)
        print(Output_Code, end = "\n")
        if(Buffer != "[]"):
            Output = Station_List(Buffer)

        #搜尋新北市各站到站資訊
        Search_URL = "https://ptx.transportdata.tw/MOTC/v2/Bus/EstimatedTimeOfArrival/City/NewTaipei%s?$format=JSON&$filter=StopName/Zh_tw eq '%s'&$orderby=RouteUID" %(RouteName, KeyWord)
        Output_Code, Buffer = Download_Task(Search_URL)
        print(Output_Code, end = "\n")
        if(Buffer != "[]"):
            Output += Station_List(Buffer)

        if(Output == ""):
            Output = "Station not found"
        return Output
    
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
