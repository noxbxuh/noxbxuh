import telebot 
import requests 
from telebot import types
from time import sleep
TOKEN = '7035041011:AAFulMQv_03VGP5XTyOrc_ZMUAuwCTztY44' 
import random
bot = telebot.TeleBot(TOKEN) 
num =0
number = "123456789101113141516171819202123242526272829"
@bot.message_handler(commands=['st'])
def send_inline_keyboard(message):
    global num
     
    button1 = types.InlineKeyboardButton(text=f'{num}', callback_data='option1')
    
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(button1)
    bot.send_message(chat_id=message.chat.id, text='Number of searches', reply_markup=keyboard)
  
@bot.message_handler(commands=['start']) 
def send_audio(message):
    global num
    
    sleep(1)
    aa = str(''.join((random.choice(number) for i in range(2))))
    a = str(''.join((random.choice(number) for i in range(1))))
    url = f'http://quran.ksu.edu.sa/ayat/mp3/Ali_Jaber_64kbps/0{aa}00{a}.mp3' 
    response = requests.get(url, verify=False) 
    if response.status_code == 200: 
       bot.send_audio(message.chat.id,response.content,caption="for me and my parents
me : @usaByte",parse_mode="html")
       num += 1
       print('Done Send file') 
    else: 
        print('Error Send file MP3.') 
 


bot.polling()

