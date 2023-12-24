import telebot , json, random 
from telebot import types

with open("dataset.json", encoding="UTF-8") as file_in:
    records = json.load(file_in)
print(records)

bot = telebot.TeleBot('')

secret_santa = {}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Добро пожаловать в бота Тайного Санты!")


@bot.message_handler(content_types='text')
def message_reply(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выбрать рандомного получателя подарка!")
    btn2 = types.KeyboardButton("Выход")
    markup.add(btn1, btn2)
    if message.text=="Выбрать рандомного получателя подарка!":
        random.randint(0,23)
        result = random.randint(0,23)
        records[result]
        bot.send_message(message.chat.id, f'Ваш рандомный получатель: {records[result]["first_name"]} {records[result]["last_name"]}, его желаемый подарок: {records[result]["gift"]}')
    elif message.text=="Выход":
        start(message)

bot.polling()