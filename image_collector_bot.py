from telebot import TeleBot, types
from simple_settings import settings

bot = TeleBot(settings.ACCESS_TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('شروع')
itembtn2 = types.KeyboardButton('خروج')
itembtn3 = types.KeyboardButton('عکس کارت ملی')
itembtn4 = types.KeyboardButton('عکس سلفی')
markup.add(itembtn2, itembtn1,
           itembtn4, itembtn3)

choose = None


def choose_button(message):
    bot.send_message(message.chat.id, settings.CHOOSE_BUTTON_MESSAGE, reply_markup=markup)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, settings.WELCOME_MESSAGE)
    choose_button(message)


# Handle photo
@bot.message_handler(content_types=['photo'])
def save_photo(message):
    global choose
    if choose:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        image_name = '%s-%d.jpg' % (choose, message.from_user.id)
        with open(image_name, 'wb') as new_file:
            new_file.write(downloaded_file)
        choose = None
        bot.send_message(message.chat.id, settings.CHOOSE_BUTTON_MESSAGE, reply_markup=markup)
    else:
        bot.send_message(message.chat.id, settings.CHOOSE_PHOTO_MESSAGE, reply_markup=markup)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global choose
    print(message)
    if message.text == 'عکس سلفی':
        choose = 'selfie'
        bot.reply_to(message, settings.SELFIE_PHOTO_MESSAGE)

    if message.text == 'عکس کارت ملی':
        choose = 'national'
        bot.reply_to(message, settings.NATIONAL_CARD_PHOTO_MESSAGE)
    if message.text == 'شروع':
        send_welcome(message)

    if message.text == 'خروج':
        bot.reply_to(message, 'با تشکر از همکاری شما.')


bot.polling()
