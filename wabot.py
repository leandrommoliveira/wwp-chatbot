import json
import requests
import datetime
from bot import Robot

class WABot():    
    def __init__(self, json):
        self.json = json
        self.dict_messages = json['messages']
        self.APIUrl = 'https://eu144.chat-api.com/instance141984/'
        self.token = 'ibr1rn0epebwdnnt'
   
    def send_requests(self, method, data):
        url = f"{self.APIUrl}{method}?token={self.token}"
        headers = {'Content-type': 'application/json'}
        answer = requests.post(url, data=json.dumps(data), headers=headers)
        return answer.json()

    def send_message(self, chatID, text):
        data = {"chatId" : chatID,
                "body" : text}  
        answer = self.send_requests('sendMessage', data)
        return answer

    def welcome(self,chatID, noWelcome = False):
        welcome_string = ''
        if (noWelcome == False):
            welcome_string = "WhatsApp Demo Bot Python\n"
        else:
            welcome_string = """Incorrect command
Commands:
1. chatid - show ID of the current chat
2. time - show server time
3. me - show your nickname
4. file [format] - get a file. Available formats: doc/gif/jpg/png/pdf/mp3/mp4
5. ptt - get a voice message
6. geo - get a location
7. group - create a group with the bot"""
        return self.send_message(chatID, welcome_string)

    def time(self, chatID):
        t = datetime.datetime.now()
        time = t.strftime('%d:%m:%Y')
        return self.send_message(chatID, time)

    def show_chat_id(self,chatID):
        return self.send_message(chatID, f"Chat ID : {chatID}")

    def me(self, chatID, name):
        return self.send_message(chatID, name)

    def file(self, chatID, format):
        availableFiles = {'doc' : 'document.doc',
                        'gif' : 'giffile.gif',
                        'jpg' : 'jpgfile.jpg',
                        'png' : 'pngfile.png',
                        'pdf' : 'presentation.pdf',
                        'mp4' : 'video.mp4',
                        'mp3' : 'mp3file.mp3'}
        if format in availableFiles.keys():
            data = {
                        'chatId' : chatID,
                        'body': f'https://domain.com/Python/{availableFiles[format]}',                      
                        'filename' : availableFiles[format],
                        'caption' : f'Get your file {availableFiles[format]}'
                    }
            return self.send_requests('sendFile', data)
    
    def ptt(self, chatID):        
            data = {
            "audio" : 'https://domain.com/Python/ptt.ogg',
            "chatId" : chatID }
            return self.send_requests('sendAudio', data)

    def geo(self, chatID):
        data = {
                "lat" : '51.51916',
                "lng" : '-0.139214',
                "address" :'Your address',
                "chatId" : chatID
        }
        answer = self.send_requests('sendLocation', data)
        return answer
    
    def group(self, author):
        phone = author.replace('@c.us', '')
        data = {
            "groupName" : 'Group with the bot Python',
                        "phones" : phone,
                        'messageText' : 'It is your group. Enjoy'
        }
        answer = self.send_requests('group', data)
        return answer
    

    def processing(self):
        if self.dict_messages != []:
            for message in self.dict_messages:
                text = message['body'].split()
                print(message['senderName'])
                if message['senderName'] == 'Tamara':
                    resp = self.responses(text)
                    answer = self.send_message(message['chatId'], resp)
                    print(answer)
                    return answer
                
                elif message['senderName'] == 'Mae':
                    resp = self.responses(text)
                    answer = self.send_message(message['chatId'], resp)
                    print(answer)
                    return answer

                # if not message['fromMe']:
                    # id  = message['chatId']
                    # if text[0].lower() == 'hi':
                    #     return self.welcome(id)
                    # elif text[0].lower() == 'time':
                    #     return self.time(id)
                    # elif text[0].lower() == 'chatid':
                    #     return self.show_chat_id(id)
                    # elif text[0].lower() == 'me':
                    #     return self.me(id, message['senderName'])
                    # elif text[0].lower() == 'file':
                    #     return self.file(id, text[1])
                    # elif text[0].lower() == 'ptt':
                    #     return self.ptt(id)
                    # elif text[0].lower() == 'geo':
                    #     return self.geo(id)
                    # elif text[0].lower() == 'group':
                    #     return self.group(message['author'])
                    # else:
                    #     return self.welcome(id, True)
                else: return 'NoCommand'

    def responses(self, text):
        if text == 'oi' or text == 'Oi' or text == 'Oie' or text == 'Olá' or text == 'Ola':
            return 'oi, tudo bem?'
        elif text == 'tudo bem e voce?' or text == 'td bem e vc?' or text == 'td sim e vc?':
            return 'bom tmb!'
        elif text == 'td bem?' or text == 'tudo bem?' or text == 'como voce esta?' or text == 'e ai blz?':
            return 'tudo bem e vc?'
        elif text == 'bem':
            return 'que bom!'
        else:
            return '?'