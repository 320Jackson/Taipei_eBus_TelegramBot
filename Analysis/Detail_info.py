import json
import os.path

def SearchTarget(TargetID, JsonObj, Mode):
    #二分搜尋路線
    IsFound = False
    Start = 0
    End = len(JsonObj) - 1
    Output = None
    
    while(IsFound != True):
        if(Start > End):
            break
        mid = Start + ((End - Start) // 2)
        #取得比對ID
        if(Mode == 0):
            Item = JsonObj[mid]['RouteID']
        elif(Mode == 1):
            Item = JsonObj[mid]['StopID']
        #二分搜尋    
        if(Item > TargetID):
            End = mid - 1
        elif(Item < TargetID):
            Start = mid + 1
        else:
            Output = JsonObj[mid]
            IsFound = True

    return Output

def getRouteInfo(RouteUID):
    #取得路線資訊檔案位置
    City = RouteUID[0:3] #取得主管機關
    RouteID = RouteUID[3:]
    db_Location = f"./RouteInfo/{City}_Route.json"

    with open(db_Location, 'r') as f:
        JsonObj = json.loads(f.read())
    
    Output = SearchTarget(RouteID, JsonObj, 0)
    return Output

def getStopInfo(StopUID):
    #取得路線檔案位置
    City = StopUID[0:3]
    StopID = StopUID[3:]
    db_Location = f"./StopInfo/{City}_Stop.json"

    with open(db_Location, 'r') as f:
        JsonObj = json.loads(f.read())
    
    Output = SearchTarget(StopID, JsonObj, 1)
    return Output