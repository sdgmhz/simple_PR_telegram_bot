import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
import os
from dotenv import load_dotenv
import random
import logging


logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

load_dotenv()
API_TOKEN = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def first_step(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder="لطفا یک مورد را انتخاب کنید", one_time_keyboard=True)
    markup.add(KeyboardButton("ارتباط مستقیم با ما"), KeyboardButton("ثبت مشکل"))
    bot.send_message(message.chat.id, "لطفا یک مورد را انتخاب کنید", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "ارتباط مستقیم با ما")
def direct_connection(message):
    contact_1_number = "0912345678"
    contact_1_name = "پشتیبانی 1"
    contact_2_number = '02177777777'
    contact_2_name = "پشتیبانی 2"
    bot.send_message(message.chat.id, "برای ارتباط مستقیم با ما می توانید با شماره ها پشتبانی که در زیر آمده است تماس حاصل نمایید:")
    bot.send_contact(message.chat.id, contact_1_number, contact_1_name)
    bot.send_contact(message.chat.id, contact_2_number, contact_2_name)


@bot.message_handler(func= lambda message: message.text == "ثبت مشکل")
def report_problem(message):
    bot.send_message(message.chat.id, "لطفا مشکل خود را وارد نمایید")
    bot.register_next_step_handler(message, assign_ref_ticket)

def assign_ref_ticket(message):
    ref_number = random.randint(111111, 999999)
    bot.reply_to(message, f"کارشناسان ما در اسرع وقت با شما تماس خواهند گرفت، شماره پیگیری تیکت {ref_number} می باشد")



bot.infinity_polling()







