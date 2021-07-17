import telebot
import time
import pyshorteners as ps

bot_token = '1927164991:AAGiiJGLXGMacJmeRvqyTEKjXVQgOU8KhYQ'
bot = telebot.TeleBot(token=bot_token)

def short(url):
    return ps.Shortener().tinyurl.short(url)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'saaam dossdar.negesiiiz ? Eger ilk defe burdasinizsa /komek yazsaniz belke komeklik ede bildim.')

@bot.message_handler(commands=['komek'])
def send_welcome(message):
    bot.reply_to(message, 'her hansi bir fayli yuklenebiler bir qisaldilmis linke cevirme qabiliyyetim var. Sadece istediyiniz seyi mene gonderin.')


@bot.message_handler(content_types='photo')
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.photo[3].file_id)))
    except AttributeError:
        pass

@bot.message_handler(content_types='video')
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.video.file_id)))
    except AttributeError:
        pass

@bot.message_handler(content_types='audio')
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.audio.file_id)))
    except AttributeError:
        pass

@bot.message_handler(content_types='document')
def file_sent(message):
    try:
        bot.send_message(message.chat.id, short(bot.get_file_url(message.document.file_id)))
    except AttributeError:
        pass

while True:
    try:
        bot.polling()
    except Exception:
        time.sleep(15)