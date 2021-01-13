
import telebot
from telebot import types
import mark
from geopy import distance
import random

bot = telebot.TeleBot("1212347030:AAGfHHfVk7thlVc_nU02eRFfA9Cn4x01Ic8")
joinedFile = open("D:/Python/list.txt", "r") 
joinedUsers = set()
for line in joinedFile:
	joinedUsers.add(line.strip())
	joinedFile.close()

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
markup_ran = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
btn_random = types.KeyboardButton ("Випадковий заклад\U0001F381")
btn_geo = types.KeyboardButton ("Найближчий заклад\U0001F50D", request_location = True)
btn_list = types.KeyboardButton ("Список закладів\U0001F4DD")
btn_other = types.KeyboardButton ("Інше\U0001F47B")
markup_menu.add(btn_random,btn_geo, btn_list, btn_other)
markup_ran.add(btn_list, btn_other)
@bot.message_handler(commands=['start',])
def send_welcome(message):
	if not message.chat.id in joinedUsers:
		joinedFile = open("D:/Python/list.txt", "a")
		joinedFile.write(str(message.chat.id) + "\n")
		joinedUsers.add(message.chat.id)
	first_name = message.chat.first_name #Ім`я
	last_name = str(message.chat.last_name) #Прізвище
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBQ6RfR8r9OHxVZxEIik6XXRVYh5StpQACBAcAAkb7rARD2NYo4qk9gxsE")
	bot.send_message(message.chat.id, "Привіт, " + first_name +" "+ last_name + "! \nЯ допоможу обати заклад у Львові, просто обери що тебе зараз цікавить:)", reply_markup=markup_menu)
@bot.message_handler(commands=["special1"])
def mess(message):
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBQ6RfR8r9OHxVZxEIik6XXRVYh5StpQACBAcAAkb7rARD2NYo4qk9gxsE")
	for user in joinedUsers:
		bot.send_message(user, message.text[message.text.find(" "):])
@bot.message_handler(content_types = ["text"])
def message(message):
	if message.text == "Випадковий заклад\U0001F381":
	
		print(random.choice(tuple(mark.institutet.keys())))
	bot.send_message(message.chat.id, "РАНДОМ", reply_markup=markup_ran)
	if message.text == "2кнопка1меню":
		user_markup2 = telebot.types.ReplyKeyboardMarkup(True,False)
		user_markup2.row("1копнка2меню 2 ответ", "2копнка2меню 2 ответ")
		bot.send_message(message.chat.id, "ответ на 2кнопка1меню", reply_markup=user_markup2)
	if message.text == "Назад":
		send_welcome(message)
@bot.message_handler(func = lambda message: True, content_types = ["location"])
def location(message) :
	lon = message.location.longitude
	lat = message.location.latitude

	key = []
	for m in mark.institutet :
		result = distance.distance((m["latm"], m["lonm"]), (lat, lon), meters = 1)
		key.append(result)
	index = key.index(min(key))
	bot.send_message(message.chat.id, "Найближчий заклад")
	bot.send_venue (message.chat.id,
					mark.institutet[index]["latm"],
					mark.institutet[index]["lonm"],
					mark.institutet[index]["title"],
					mark.institutet[index]["adress"])


	
	
bot.polling()
