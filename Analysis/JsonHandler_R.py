import json
import os.path

def LoadDetail(Region, RouteName):
    RouteDetail = {}
    with open(f"./RouteMap/{Region}_RouteMap.json", 'r') as f:
        RouteDetail = json.loads(f.read())
    Output = None
    for Run in RouteDetail:
        if(Run['RouteName']['Zh_tw'] == RouteName):
            Output = Run
            break
    return Output

def getRouteDetail(RouteName):
    Output = LoadDetail("TPE", RouteName)
    if(Output == None):
        Output = LoadDetail("NWT", RouteName)
        
    return Output


def Analysis_StationMoving(RouteName, StaData, BusData, Direction):
    MovingObj = json.loads(StaData)
    BusMoving  = json.loads(BusData)
    RouteDetail = getRouteDetail(RouteName)

    print(RouteDetail)

    


