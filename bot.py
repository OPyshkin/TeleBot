import telebot
from telebot.types import Message
TOKEN = '675804825:AAEePWNE3Xj5Sh0CyPrDuxsKmVnXk0MmyGI'
STICKER_ID = 'CAADAgADQgEAAtnvCQABO3kaFw67_pYC'
golovka= 'CAADBAADjgEAAjPl4hUvI3VlUsQgtAI'
plecho = 'CAADBAADjwEAAjPl4hU0OKNGHbQi-QI'
na= 'CAADBAADkAEAAjPl4hWDiyIDoeXKxQI'
minet = 'CAADBAADkQEAAjPl4hUAATXKzK6Do7IC'
noga = 'CAADBAADkgEAAjPl4hWqAbtFfYNHTAI'
pizda = 'CAADBAADkwEAAjPl4hVchh0Om9EItgI'
govne = 'CAADBAADlAEAAjPl4hWDe5gGCZpsOQI'

bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands = ['start', 'help'])
def command_handler(message: Message):
    bot.reply_to(message, 'No answer')

@bot.message_handler(content_types = ['text', 'sticker'])
def echo_digits(message: Message):
    '''if message.text == 'Нет' or 'нет':
       bot.reply_to(message, 'Пидора ответ!')
       return'''
    if message.text == 'я' or message.text ==  'Я':
        bot.send_sticker(message.chat.id, golovka)
        return
    elif message.text == 'Че?' or message.text ==  'Чё?'or message.text == 'че?'or message.text == 'чё?'or message.text ==  'Че'or message.text == 'Чё'or message.text == 'чё'or message.text == 'че':
        bot.send_sticker(message.chat.id, plecho)
        return
    elif message.text == 'А?' or message.text == 'а?'or message.text == 'А'or message.text == 'а':
        bot.send_sticker(message.chat.id, na)
        return
    elif message.text == 'Нет' or message.text == 'нет':
        bot.send_sticker(message.chat.id, minet)
        return
    elif message.text == 'ааа' or message.text == 'ААА':
        bot.send_sticker(message.chat.id, noga,reply_to_message_id=message.message_id)
        return
    elif message.text == 'Да' or message.text == 'да':
        bot.send_sticker(message.chat.id, pizda)
        return
    elif message.text == 'Не' or message.text == 'не'or message.text == 'Не?'or message.text == 'не?':
        bot.send_sticker(message.chat.id, govne)
        return
    elif 'пантера круто' in message.text or 'Пантера круто' in message.text:
        bot.reply_to(message, 'говно!')
        return
    elif 'мамку ебал' in message.text or 'Мамку ебал' in message.text:
        bot.reply_to(message, 'Нет я!')
        return
    elif 'ты пидор' in message.text or 'Ты пидор' in message.text:
        bot.reply_to(message, 'Нет ты!' )
        return
    

@bot.message_handler(content_types=['sticker'])
def sticker_handler(message: Message):
    pass
bot.polling()
