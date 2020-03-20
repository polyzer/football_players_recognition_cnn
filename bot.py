import telebot
import tensorflow as tf
import cv2
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import re
import json
import decorator

bot = telebot.TeleBot('1045675720:AAGV3UhR4Ks4mkV-x1ZTfjF8et0Iudp3hbk')

@decorator.decorator
def errLog(func, *args, **kwargs):
    result = None
    try:
        result = func(*args, **kwargs)
    except Exception as e:
        print(e.__repr__())
    return result


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

@errLog
def processPhotoMessage(message):
    print('message.photo =', message.photo)
    fileID = message.photo[-1].file_id
    print('fileID =', fileID)
    file = bot.get_file(fileID)
    print('file.file_path =', file.file_path)
    downloaded_file = bot.download_file(file.file_path)
    # downloaded_file = cv2.fromarray(downloaded_file)
    # img = cv2.imdecode(downloaded_file, 1)
    with open("image.png", 'wb') as new_file:
        new_file.write(downloaded_file)
    img = cv2.imread("image.png")
    plt.imshow(img)
    plt.show()

@bot.message_handler(content_types=['photo'])
def photo(message):
    processPhotoMessage(message)

print("it's started")
bot.polling()