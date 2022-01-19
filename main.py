import os
import time
import telebot
from telebot import types
from pytube import YouTube

my_secret = os.environ['API_KEY']


TOKEN = my_secret
knownUsers = []  # todo: save these in a file,
userStep = {}  # so they won't reset every time the bot restarts

commands = {  # command description used in the "help" command
    'start'       : 'Get used to the bot \n',
    'help'        : 'Gives you information about the available commands \n',
    'sendLongText': 'A test using the \'send_chat_action\' command \n',
    'getImage'    : 'A test using multi-stage messages, custom keyboard, and media sending \n',
    '/Type yt-download' : 'To Download YT Videos for Free \n'
    
}

imageSelect = types.ReplyKeyboardMarkup(one_time_keyboard=True)  # create the image selection keyboard
imageSelect.add('Mickey', 'Minnie','Books')

hideBoard = types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard


# error handling if user isn't known yet
# (obsolete once known users are saved to file, because all users
#   had to use the /start command and are therefore known to the bot)
def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected, who hasn't used \"/start\" yet")
        return 0


# only used for console output now
def listener(messages):
    """
    When new messages arrive TeleBot will call this function.
    """
    for m in messages:
        if m.content_type == 'text':
            # print the sent message to the console
            print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + m.text)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)  # register listener


# handle the "/start" command
@bot.message_handler(commands=['start'])
def command_start(m):
    cid = m.chat.id
    if cid not in knownUsers:  # if user hasn't used the "/start" command yet:
        knownUsers.append(cid)  # save user id, so you could brodcast messages to all users of this bot later
        userStep[cid] = 0  # save user id and his current "command level", so he can use the "/getImage" command
        bot.send_message(cid, "Hello, stranger, let me scan you...")
        bot.send_message(cid, "Scanning complete, I know you now")
        command_help(m)  # show the new user the help page
    else:
        bot.send_message(cid, "I already know you, no need for me to scan you again!")


# help page
@bot.message_handler(commands=['help'])
def command_help(m):
    cid = m.chat.id
    help_text = "The following commands are available: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page

@bot.message_handler(func=lambda message: message.text.lower() == "yt")
def command_help(m):
    cid = m.chat.id
    bot.send_message(m.chat.id,"Please send the Url of the video")
    @bot.message_handler(func=lambda message: True, content_types=['text'])
    def ytube_download(m):
        bot.send_message(m.chat.id, "Please Wait,Video on the way")
        link = m.text
        yt = YouTube(link)
        print("Title: ",yt.title)
        yt.streams.first().download()
        os.rename(yt.streams.first().default_filename, 'download.mp4')
        bot.send_message(m.chat.id, "Video on the way")
        bot.send_document(cid, open('download.mp4', 'rb'))

    bot.send_message(cid, m.text)





# user can chose an image (multi-stage command example)





  
bot.set_update_listener(listener)
bot.infinity_polling()