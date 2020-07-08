from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot import ChatBot

class Robot():
    def __init__(self):
        self.bot = ChatBot(
            'R2D2',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///database.sqlite3'
        )

        self.conversa = ChatterBotCorpusTrainer(self.bot)
        self.conversa.train('./custom.yml')

    def getAnwser(self, text):
        try:
            response = self.bot.get_response(text)
            if float(response.confidence) > 0.5:
                return response
            
            return '?'

        except:
            return '??'