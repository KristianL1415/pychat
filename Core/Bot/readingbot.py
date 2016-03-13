# ReadingBot.py

import bot
import time


class ReadingBot(bot):
    def __init__(self):
        print 'init'

    def process(self, message):
        super.process(message)
        time.sleep(1)