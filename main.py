#!/usr/bin/python
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
bot = ChatBot('ChatterBot')
bot.set_trainer(ListTrainer)
while True:
    text = raw_input('You: ')
    if (text=="bye"):
        print("Have a good day!! Bye")
        break
    response = bot.get_response(text)
    response = str(response)
    print('Bot: ' + response)
