from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton
import time
from datetime import datetime, timedelta
from db import Deadlines

bot = TeleBot("1114535076:AAFCnD1VMmFaj5hdpAosKtrTgLjkkJHCQFA")

def current(text):
    parse = text.split(' ')
    if parse[-1].find('+') != -1 or parse[-2].find('+') != -1:
        now = datetime.today()
        if parse[-1].find('+') != -1:
            shift = timedelta(int(parse[-1][1:]))
            name = ' '.join(parse[:len(parse)-1])
            return name, now + shift, 0
        else:
            shift = timedelta(int(parse[-2][1:]))
            name = ' '.join(parse[:len(parse)-2])
            return name, now + shift, 1

@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, text='Hello world')


@bot.message_handler(content_types=["text"])
def new_deadline(msg):
    deadline, time, repeat = current(msg.text)
    bot.send_message(msg.chat.id, text='Дедлайн назначен!')
    dd = Deadlines.create(id = msg.chat.id, name = deadline, date = time, repeat = repeat)
    dd.save()


try:
    bot.polling(none_stop=True)
except:
    time.sleep(10)