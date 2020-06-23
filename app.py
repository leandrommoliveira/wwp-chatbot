import os
from flask import Flask, request, jsonify
from wabot import WABot
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def nao_entre_em_panico():
    if request.headers.get('Authorization') == '42':
        return jsonify({"42": "a resposta para a vida, o universo e tudo mais"})
    return jsonify({"message": "Não entre em pânico!"})

@app.route('/', methods=['POST'])
def home():
    if request.method == 'POST':
        bot = WABot(request.json, app.logger)
        return bot.processing()

if(__name__) == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)