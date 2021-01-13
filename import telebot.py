import telebot

bot = telebot.TeleBot("1212347030:AAGfHHfVk7thlVc_nU02eRFfA9Cn4x01Ic8")
joinedFile = open("D:/Python/list.txt","r") 
joinedUsers = set()
for line in joinedFile:
	joinedUsers.add(line.strip())
	joinedFile.close()

markup_menu =types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
btn_random = types.KeyboardButton ("Випадковий заклад\U0001F381")
btn_geo = types.KeyboardButton ("Найближчий заклад\U0001F50D", request_location = True)
btn_list = types.KeyboardButton ("Список закладів\U0001F4DD")
btn_other= types.KeyboardButton ("Інше\U0001F47B")
@bot.message_handler(commands=['start',])
def send_welcome(message):
	if not message.chat.id in joinedUsers:
		joinedFile = open("D:/Python/list.txt","a")
		joinedFile.write(str(message.chat.id) + "\n")
		joinedUsers.add(message.chat.id)
	first_name = message.chat.first_name #Ім`я
	last_name = str(message.chat.last_name) #Прізвище
	main_menu_markup = telebot.types.ReplyKeyboardMarkup(True,False)
	main_menu_markup.row("Випадковий заклад\U0001F381", "Найближчий заклад\U0001F50D",)
	main_menu_markup.row("Список закладів\U0001F4DD")
	main_menu_markup.row("Інше\U0001F47B")
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBQ6RfR8r9OHxVZxEIik6XXRVYh5StpQACBAcAAkb7rARD2NYo4qk9gxsE")
	bot.send_message(message.chat.id, "Привіт, " + first_name +" "+ last_name + "! \nЯ допоможу обати заклад у Львові, просто обери що тебе зараз цікавить:)", reply_markup=main_menu_markup)
@bot.message_handler(content_types = ["text"])
def message(message):
	if message.text == "Випадковий заклад\U0001F381":
		request_location = True
		user_markup1 = telebot.types.ReplyKeyboardMarkup(True,False)
		user_markup1.row("1копнка2меню 1 ответ", "2копнка2меню 1 ответ") 
		user_markup1.row("Назад")
		bot.send_message(message.chat.id, "ответ на 1кнопка1меню", reply_markup=user_markup1)
	if message.text == "2кнопка1меню":
		user_markup2 = telebot.types.ReplyKeyboardMarkup(True,False)
		user_markup2.row("1копнка2меню 2 ответ", "2копнка2меню 2 ответ")
		bot.send_message(message.chat.id, "ответ на 2кнопка1меню", reply_markup=user_markup2)
	if message.text == "Назад":
		send_welcome(message)

 
@bot.message_handler(commands=["sendspecial"])
def mess(message):
	for joiedUsers in joinedUsers:
		bot.send_message(joinedUsers, message.text[message.text.find(""):])

bot.polling()





