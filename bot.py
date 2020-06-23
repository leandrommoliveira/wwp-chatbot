from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Robot():
    def __init__(self):
        self.bot = ChatBot(
            'C3PO',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            database_uri='sqlite:///database.sqlite3'
        )

        self.trainner = ChatterBotCorpusTrainer(self.bot)
        self.trainner.train("./custom.yml")


    def getAnwser(self, text):
        try:
            response = self.bot.get_response(text)
            if float(response.confidence) > 0.5:
                return response
            
            return '?'

        except:
            print("Exception buscando uma resposta")
            return '??'