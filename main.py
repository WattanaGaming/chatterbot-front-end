#!/usr/bin/python
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('ChatterBot')

bot.set_trainer(ListTrainer)

while True:
    text = raw_input('You: ')
    response = bot.get_response(text)
    response = str(response)

    print('Bot: ' + response)
