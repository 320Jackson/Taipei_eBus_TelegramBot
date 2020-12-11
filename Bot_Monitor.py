import time

def MessageMonitor(msg):    
    Content = ""
    try:
        Content = msg['text']
    except:
        Content = "Other Type"
    
    chat_id = msg['chat']['id'] #Chat ID
    chat_Type = msg['chat']['type'] #Type

    chat_from = "" #Chat From
    if(chat_Type == "supergroup" or chat_Type == "group"):
        chat_from = msg['chat']['title']
    else:
        chat_from = msg['chat']['first_name'] + " " + msg['chat']['last_name']

    try:
        User = msg['from']['username'] #From who
    except:
        User = msg['from']['first_name'] + " " + msg['from']['last_name']
    
    UploadTime = time.asctime(time.localtime(time.time()))
    print("%s\n%s\n%s\n%s\n%s\n%s" %(Content, chat_id, chat_Type, chat_from, User, UploadTime))