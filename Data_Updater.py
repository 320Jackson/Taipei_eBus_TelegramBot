from WebTask.Web_Crawler import Download_Task

def SaveContent(Path, Content):
    with open(Path, 'w') as f:
        f.write(Content)

def RouteInfo_Updater():
    Path = "./RouteInfo/TPE_Route.json"
    StatusCode, Buffer = Download_Task("https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/Taipei?$format=JSON")
    print(f"臺北市路線資訊Status:{StatusCode}")
    SaveContent(Path, Buffer)

    Path = "./RouteInfo/NWT_Route.json"
    print(f"新北市路線資訊Status:{StatusCode}")
    StatusCode, Buffer = Download_Task("https://ptx.transportdata.tw/MOTC/v2/Bus/Route/City/NewTaipei?$format=JSON")
    SaveContent(Path, Buffer)

def RouteMap_Updater():
    Path = "./RouteInfo/TPE_RouteMap.json"
    StatusCode, Buffer = Download_Task("https://ptx.transportdata.tw/MOTC/v2/Bus/StopOfRoute/City/Taipei?$format=JSON")
    print(f"臺北市路線資訊Status:{StatusCode}")
    SaveContent(Path, Buffer)

    Path = "./RouteInfo/NWT_RouteMap.json"
    print(f"新北市路線資訊Status:{StatusCode}")
    StatusCode, Buffer = Download_Task("https://ptx.transportdata.tw/MOTC/v2/Bus/StopOfRoute/City/NewTaipei?$format=JSON")
    SaveContent(Path, Buffer)

def StationInfo_Updater():
    Path = "./RouteInfo/TPE_Station.json"
    StatusCode, Buffer = Download_Task("https://ptx.transportdata.tw/MOTC/v2/Bus/Station/City/Taipei?$format=JSON")
    print(f"臺北市路線資訊Status:{StatusCode}")
    SaveContent(Path, Buffer)

    Path = "./RouteInfo/NWT_Station.json"
    print(f"新北市路線資訊Status:{StatusCode}")
    StatusCode, Buffer = Download_Task("https://ptx.transportdata.tw/MOTC/v2/Bus/Station/City/NewTaipei?$format=JSON")
    SaveContent(Path, Buffer)

def StopInfo_Updater():
    Path = "./RouteInfo/TPE_Stop.json"
    StatusCode, Buffer = Download_Task("https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/Taipei?$format=JSON")
    print(f"臺北市路線資訊Status:{StatusCode}")
    SaveContent(Path, Buffer)

    Path = "./RouteInfo/NWT_Stop.json"
    print(f"新北市路線資訊Status:{StatusCode}")
    StatusCode, Buffer = Download_Task("https://ptx.transportdata.tw/MOTC/v2/Bus/Stop/City/NewTaipei?$format=JSON")
    SaveContent(Path, Buffer)