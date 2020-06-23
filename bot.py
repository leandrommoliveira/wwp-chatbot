from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

class Robot():
    def __init__(self):
        self.bot = ChatBot('TW Chat Bot')
        self.conversa = ListTrainer(self.bot)
        self.conversa.train(['Oie', 'oi td bem?' ,'oi', 'oi', 'Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'td bem?', 'Sim e vc?', 'tudo sim e vc?', 'bom tmb'])

    def getAnwser(self, text):
        try:
            response = self.bot.get_response(text)
            if float(response.confidence) > 0.5:
                return response
            
            return '?'

        except:
            print("Exception buscando uma resposta")
            return '??'