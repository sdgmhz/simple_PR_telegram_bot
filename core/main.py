import telebot
import os
from dotenv import load_dotenv
import logging


logger = telebot.logger
telebot.logger.setLevel(logging.INFO)

load_dotenv()
API_TOKEN = os.environ.get("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)






bot.infinity_polling()







