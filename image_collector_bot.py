from telebot import TeleBot, types
from simple_settings import settings

bot = TeleBot(settings.ACCESS_TOKEN)

# Define a markup to better interface
markup = types.ReplyKeyboardMarkup(row_width=2)
itembtn1 = types.KeyboardButton('شروع')
itembtn2 = types.KeyboardButton('خروج')
itembtn3 = types.KeyboardButton('عکس کارت ملی')
itembtn4 = types.KeyboardButton('عکس سلفی')
markup.add(itembtn2, itembtn1,
           itembtn4, itembtn3)

# Define a global varible for check whether user specify the photo name or not.
photo_name = None


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, settings.WELCOME_MESSAGE)
    bot.send_message(message.chat.id, settings.RIGHT_SAMPLE_MESSAGE, reply_markup=markup)
    photo = open('data_set/sample.png', 'rb')
    bot.send_photo(message.chat.id, photo)
    bot.send_message(message.chat.id, settings.CHOOSE_BUTTON_MESSAGE, reply_markup=markup)


# Handle photo
@bot.message_handler(content_types=['photo'])
def save_photo(message):
    global photo_name
    if photo_name:
        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)

        image_path = 'data_set/%s-%d.jpg' % (photo_name, message.from_user.id)
        with open(image_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # todo write in hdfs.
        # hdfsclient = InsecureClient(settings.HDFS_URL, user='m.seifikar')
        # hdfsclient.upload(settings.HDFS_DATA_PATH, image_name)

        photo_name = None
        bot.send_message(message.chat.id,
                         settings.CHOOSE_BUTTON_MESSAGE,
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id,
                         settings.CHOOSE_PHOTO_MESSAGE,
                         reply_markup=markup)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    global photo_name
    if message.text == 'عکس سلفی':
        photo_name = 'selfie'
        bot.reply_to(message, settings.SELFIE_PHOTO_MESSAGE)

    if message.text == 'عکس کارت ملی':
        photo_name = 'national'
        bot.reply_to(message, settings.NATIONAL_CARD_PHOTO_MESSAGE)
    if message.text == 'شروع':
        send_welcome(message)

    if message.text == 'خروج':
        bot.reply_to(message, 'با تشکر از همکاری شما.')


bot.polling()
