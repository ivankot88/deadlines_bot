from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton
import datetime,time
from db import Deadlines

bot = TeleBot("1114535076:AAFCnD1VMmFaj5hdpAosKtrTgLjkkJHCQFA")


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, text='Goodbye world')


@bot.message_handler(content_types=["text"])
def new_deadline(msg):
    deadline, time = msg.text.split('#')
    bot.send_message(msg.chat.id, text='Дедлайн назначен!')
    time = datetime.time(int(time[0:2]), int(time[3:5]))
    dd = Deadlines.create(id = msg.chat.id,text = deadline,time = time)
    dd.save()


try:
    bot.polling(none_stop=True)
except:
    time.sleep(10)