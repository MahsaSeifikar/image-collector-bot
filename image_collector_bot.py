from telebot import TeleBot, types
from simple_settings import settings

bot = TeleBot(settings.ACCESS_TOKEN)
markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, row_width=1)
markup.add("Read-Wiki", "Skip")


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, settings.WELCOME_MESSAGE)


# Handle photo
@bot.message_handler(content_types=['photo'])
def save_photo(message):
    fileID = message.photo[-1].file_id
    file_info = bot.get_file(fileID)
    downloaded_file = bot.download_file(file_info.file_path)
    with open("test%d.jpg" % message.message_id, 'wb') as new_file:
        new_file.write(downloaded_file)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    print(message)
    bot.reply_to(message, message.text)


counter = 1
bot.polling()
