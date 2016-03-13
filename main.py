# main.py

from Core.PyChat import PyChat

def main():
    # add arg for learning mode
    print 'main'
    bot = PyChat()
    bot.mode = 'chat'
    bot.start()

if __name__ == "__main__":
    main()
