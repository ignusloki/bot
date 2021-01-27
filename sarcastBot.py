from telegram.ext import Updater, InlineQueryHandler, CommandHandler, Filters
from requests.exceptions import ConnectionError
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def sarcasmo(update, context):
    url = get_url()
    context.bot.sendPhoto(
      chat_id=update.effective_chat.id, photo='https://static.wikia.nocookie.net/bigbangtheory/images/8/8b/Leonard_holds_sarcasm_sign.jpg/revision/latest/scale-to-width-down/318?cb=20121009192217'
    )


def pikachu(update, context):
    url = get_url()
    context.bot.sendPhoto(
      chat_id=update.effective_chat.id, photo='https://cdn.dicionariopopular.com/imagens/46482723-914713205554017-4832741937838555136-n-cke.jpg'
    )
	

def trap(update, context):
    url = get_url()
    context.bot.sendPhoto(
      chat_id=update.effective_chat.id, photo='https://media1.giphy.com/media/Z1LYiyIPhnG9O/giphy.gif?cid=ecf05e47tt1g2w2rwydxqezmyaw4ojuu7weoo7ygbgqqcq33&rid=giphy.gif'
    )


def main():
    updater = Updater('1449834468:AAFbcYaczBRFsMWnDDvA7pfcW7MWVGyKVuA')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('sarcasmo',sarcasmo))
    dp.add_handler(CommandHandler('s',sarcasmo))
    dp.add_handler(CommandHandler('pikachu',pikachu))
    dp.add_handler(CommandHandler('trap',trap))
	
    while True:
        try:
            updater.start_polling()

        except Exception as e:
            logger.error(e)  # or just print(e) if you don't have logger,
            # or import traceback; traceback.print_exc() for print full info
            time.sleep(15)
            
    updater.idle()
	
def start(update, context):
    response_message = "Eu fui criado para indicar sarcasmo para os Sheldons do grupo!"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=response_message
    )
	
def unknown(update, context):
    response_message = "Bazinga?"
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=response_message
    )

if __name__ == '__main__':
    main()