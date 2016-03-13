# ChatBot.py

import bot
import time


class ChatBot(bot):
    def __init__(self):
        print 'init'

    def process(self, message):
        super.process(message)
        time.sleep(1)
