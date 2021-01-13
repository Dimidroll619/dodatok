import telebot

bot = telebot.TeleBot("1212347030:AAGfHHfVk7thlVc_nU02eRFfA9Cn4x01Ic8")
joinedFile = open("D:/Python/list.txt","r") 
joinedUsers = set()
for line in joinedFile:
	joinedUsers.add(line.strip())
	joinedFile.close()

@bot.message_handler(commands=['start',])
def send_welcome(message):
	if not message.chat.id in joinedUsers:
		joinedFile = open("D:/Python/list.txt","a")
		joinedFile.write(str(message.chat.id) + "\n")
		joinedUsers.add(message.chat.id)
		bot.send_message(message.chat.id, "Привіт, "

@bot.message_handler(commands=["special"])
def mess(message):
	for user in joinedUsers:
		bot.send_message(user, message.text[message.text.find(""):])

bot.polling()

