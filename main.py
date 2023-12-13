import telebot
from telebot import types

bot = telebot.TeleBot('')

secret_santa = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Добро пожаловать в бота Тайного Санты!")
    bot.send_message(message.chat.id, "Пожалуйста, введите свое имя.")
    bot.register_next_step_handler(message, ask_name)

def ask_name(message):
    chat_id = message.chat.id
    name = message.text
    secret_santa[chat_id] = {'name': name}
    bot.send_message(chat_id, "Отлично, {}, введите имя получателя подарка:".format(name))
    bot.register_next_step_handler(message, ask_recipient)

def ask_recipient(message):
    chat_id = message.chat.id
    recipient = message.text
    secret_santa[chat_id]['recipient'] = recipient
    bot.send_message(chat_id, "Спасибо! Теперь вы участвуете в игре Тайный Санта.")
    bot.send_message(chat_id, "Вы были выбраны для дарения подарка пользователю {}.".format(recipient))

@bot.message_handler(commands=['reveal'])
def reveal(message):
    chat_id = message.chat.id
    if chat_id in secret_santa:
        recipient = secret_santa[chat_id]['recipient']
        bot.send_message(chat_id, "Ваш получатель подарка - {}.".format(recipient))
    else:
        bot.send_message(chat_id, "Вы еще не участвуете в игре Тайный Санта.")

bot.polling()