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
        self.bot = Robot()
   
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
                #verifica o nome de quem esta enviando a mensagem, a verificação pode ser feita por id tambem
                if message['senderName'] == 'Teste':
                    answer = self.bot.getAnwser(text)
                    response = self.send_message(message['chatId'], answer)
                    print(response)
                    return response

                else: return 'NoCommand'