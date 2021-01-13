import telepot
from telepot.loop import OrderedWebhook
from flask import Flask, request
import configparser #Config File
import time
#Bot Monitor
from Bot_Monitor import MessageMonitor
#Bot Command
from Command_Handler import eBusCommand
import logging

FormatStr = f"[%(asctime)s] %(levelname)s : %(message)s"
#logging.basicConfig(filename = "./Bot.log", filemode = 'a', format = FormatStr)

#Webhook Object
WebApp = Flask(__name__)

#Config object
Config = configparser.ConfigParser()
Config.read("Config.ini")

#Bot object
Bot = telepot.Bot(Config['TELEGRAM']['ACCESS_TOKEN'])

@WebApp.route('/hook', methods = ["POST"])
def HandleHook():
    BotHandler.feed(request.data)
    return '200 OK'

def Handler(msg):
    #Get message detail
    MessageMonitor(msg)
    
    chat_id = msg['chat']['id'] #Chat ID
    text = msg['text'] #Message Text

    #Split Command
    text = text.strip()
    textBuffer = text.split(' ')
    #Station/Bus Function
    if(textBuffer[0] == '/station' or textBuffer[0] == '/bus' or textBuffer[0] == '/station@NHITC_Bot' or textBuffer[0] == '/bus@NHITC_Bot'):        
        replyStr = ""
        if(len(textBuffer) >= 2):
            TextStr = textBuffer[1]
            replyStr = eBusCommand(textBuffer)
        else:
            replyStr = 'Please enter the key word.'
        #傳送訊息
        try:
            Bot.sendMessage(chat_id, replyStr)
        except:
            Bot.sendMessage(chat_id, replyStr)

    elif(textBuffer[0] == '/route' or textBuffer[0] == '/route@NHITC_Bot'):
        replyStr = []
        if(len(textBuffer) >= 2):
            Buffer = eBusCommand(textBuffer)
            replyStr = Buffer.split('/')
        else:
            replyStr.append("Please enter the key word.")

        for Run in replyStr:
            #傳送訊息
            try:
                Bot.sendMessage(chat_id, Run)
            except:
                Bot.sendMessage(chat_id, Run)    
    
    print("\n")

BotHandler = OrderedWebhook(Bot, Handler)

if __name__ == '__main__':
    BotHandler.run_as_thread()
    WebApp.run(host = "0.0.0.0", port = 5000)