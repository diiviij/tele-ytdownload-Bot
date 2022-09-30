<h1 align="left">telebot 0.0.4</h1>
<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" width="52" alt="python logo"  />

  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/selenium/selenium-original.svg" height="40" width="52" alt="python logo"  />
</div>

###

<h2 align="left">To Install the telebot, Please follow the steps below:</h2>
###

<p align="left">1) open cmd <br> 2) type "pip install telebot" (If you have pip on your system)<br>   3) Open Telegram 4)Chat with the BotFather to get your API key<br> 5) Setting up the bot’s gems and directory <br> 6) Let's begin coding :-)</p>

###




Example Setup
^^^^^^^^^^^^^
::

 from telebot import TeleBot

 app = TeleBot(__name__)


 @app.route('/command ?(.*)')
 def example_command(message, cmd):
     chat_dest = message['chat']['id']
     msg = "Command Recieved: {}".format(cmd)

     app.send_message(chat_dest, msg)


 @app.route('(?!/).+')
 def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']

    msg = "Parrot Says: {}".format(user_msg)
    app.send_message(chat_dest, msg)


 if __name__ == '__main__':
     app.config['api_key'] = 'xxxxxxxx:enterYourBotKeyHereToTest'
     app.poll(debug=True)


###
