# PyChat.py

import time
import bot
import ChatBot
import ReadingBot


class PyChat(self):
    def __init__(self, mode):
        self.mode = mode
        self.bot = bot()

    def start(self):
        message = raw_input('type a message or Q/q to quit: ')

        if self.mode == 'chat':
            self.bot = ChatBot()
        elif self.mode == 'reading':
            self.bot = ReadingBot()

        while True:
            if message.lower() == 'q':
                print 'goodbye'
                exit(0)

            self.bot.processMessage(message)
