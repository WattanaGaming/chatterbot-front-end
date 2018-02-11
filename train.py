#!/usr/bin/python
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('train')

bot.set_trainer(ListTrainer)

for _file in os.listdir('training'):
    chats = open('training/' + _file, 'r').readlines()
    bot.train(chats)
