import telebot
from telebot import types
import random



bot = telebot.TeleBot("1417831455:AAEXoPuUxO69Djha87hHQK09qjUnt0iWsAM") #токен
#клавиатура
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
markup_film = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
markup_write = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard=True, row_width = 1)
markup_game = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
markup_ggame = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
btn_film = types.KeyboardButton ("Выбрать фильм для просмотра\U0001F3A5")
btn_music = types.KeyboardButton ("Послушать музыку\U0001F3A7")
btn_game = types.KeyboardButton ("Поиграем?\U0001F3AE")
btn_sos = types.KeyboardButton ("\U0001F198SOS\U0001F198", request_location = True)
btn_help = types.KeyboardButton ("Совсем скучно?\U0001F614")
btn_vidomi = types.KeyboardButton ("Известные тебе фильмы и сериалы\U0001F4FA")
btn_nevidomi = types.KeyboardButton ("Рекомендации\U0001F50D")
btn_back = types.KeyboardButton ("Назад")
btn_write = types.KeyboardButton ("Написать")
btn_rock = types.KeyboardButton ("\U0000270A")
btn_scissors = types.KeyboardButton ("\U0000270B")
btn_papper = types.KeyboardButton ("\U0000270C")
btn_ggame = types.KeyboardButton ("/game")
markup_menu.add(btn_film, btn_music, btn_game, btn_help, btn_sos)
markup_film.add(btn_vidomi, btn_nevidomi, btn_back)
markup_write.add(btn_write, btn_back)
markup_game.add(btn_rock, btn_scissors, btn_papper, btn_back)
markup_ggame.add(btn_ggame,  btn_back)


@bot.message_handler(commands=['start',])
def send_welcome(message):
	first_name = message.chat.first_name #Ім`я
	last_name = str(message.chat.last_name) #Прізвище
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvAhf7ijAAh3PymbLbclu_lbhVmmDyQACBQAD9xeBK95mq4g2GUDbHgQ")
	bot.send_message(message.chat.id, "Привет, " + first_name +" "+ last_name + "! \nМеня зовут Федька, я создан поднимать тебе настроение \nЭто пилотная версия,в случае если тебе понравиться, мои способности будут разширены)", reply_markup=markup_menu)

@bot.message_handler(content_types = ["text"])
def message(message):
	if message.text == "Выбрать фильм для просмотра\U0001F3A5":
		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvFNf7yIJlZkFfJMK2prN8uv8fFwoAAMRAAP3F4Er671geDxP86geBA")
		bot.send_message(message.chat.id, "В категориях будет выпадать случайный фильм или сериал", reply_markup=markup_film)
	if message.text == "Известные тебе фильмы и сериалы\U0001F4FA":
		dir1 = ["https://novy.tv/wp-content/uploads/sites/96/2015/02/mpn.jpg", 
		"https://tryserial.name/uploads/posts/2017-07/1499750326-1636567133-voroniny-tryserial.com.jpg", 
		"https://vokrug-tv.ru/pic/product/5/2/a/2/52a27d35a0ffc646b7a25bd8cbf5a120.jpeg",
		"https://vokrug-tv.ru/pic/product/5/2/a/2/52a27d35a0ffc646b7a25bd8cbf5a120.jpeg",
		"https://vokrug-tv.ru/pic/product/5/2/a/2/52a27d35a0ffc646b7a25bd8cbf5a120.jpeg",
		"https://vokrug-tv.ru/pic/product/5/2/a/2/52a27d35a0ffc646b7a25bd8cbf5a120.jpeg"]
		film1 = random.choice(dir1)
		bot.send_photo(message.from_user.id, film1)
	if message.text == "Рекомендации\U0001F50D":
		dir2 = ["https://proprikol.ru/wp-content/uploads/2019/06/kartinki-krasivyh-devushek-skachat-besplatno-2.jpg", 
		"https://memax.club/wp-content/uploads/2019/05/1-56.jpg", 
		"https://vokrug-tv.ru/pic/product/5/2/a/2/52a27d35a0ffc646b7a25bd8cbf5a120.jpeg"]
		film2 = random.choice(dir2)
		bot.send_photo(message.from_user.id, film2)	
		
	if message.text == "Послушать музыку\U0001F3A7":
		dir3 = ["https://su.muzmo.cc/get/music/20201210/Klava_Koka_-_Pyanuyu_domojj_71911012.mp3",
		"http://d.zaix.ru/88a9392ea.MP3",
		"https://su.muzmo.cc/get/music/20201128/KHABIB_-_YAgoda_malinka_71770520.mp3",
		"https://su.muzmo.cc/get/music/20201212/NILETTO_-_nevyvoZIMAya_71937924.mp3"]
		mus = random.choice(dir3)
		bot.send_document(message.from_user.id, mus)	



	if message.text == "Поиграем?\U0001F3AE":
		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvdRf818dGfnlvYLCwfPcSPUaOo8-igACgQMAAm2wQgOxqAABZxcolQABHgQ")
		bot.send_message(message.chat.id, "Будем играть в \"камень, ножницы, бумага\"", reply_markup=markup_game)
	if message.text == "\U0000270A":
		cyefa = ["\U0000270A", "\U0000270B", "\U0000270C"]
		comp = random.choice(cyefa)
		if comp == "\U0000270A":
			win = 0
		if comp == "\U0000270B":
			win = 1
		if comp == "\U0000270C":
			win = 2
		if win == 0:
			bot.send_message(message.chat.id, "Я выбрал Камень")
			bot.send_message(message.chat.id, "Ничья")
		if win == 1:
			bot.send_message(message.chat.id, "Я выбрал Ножницы")
			bot.send_message(message.chat.id, "Ты победила")
		if win == 2:
			bot.send_message(message.chat.id, "Я выбрал Бумагу")
			bot.send_message(message.chat.id, "Ты проиграла")

	if message.text == "\U0000270B":
		cyefa = ["\U0000270A", "\U0000270B", "\U0000270C"]
		comp = random.choice(cyefa)
		if comp == "\U0000270A":
			win = 2
		if comp == "\U0000270B":
			win = 0
		if comp == "\U0000270C":
			win = 1
		if win == 2:
			bot.send_message(message.chat.id, "Я выбрал Камень")
			bot.send_message(message.chat.id, "Ты проиграла")
		if win == 0:
			bot.send_message(message.chat.id, "Я выбрал Ножницы")
			bot.send_message(message.chat.id, "Ничья")
		if win == 1:
			bot.send_message(message.chat.id, "Я выбрал Бумагу")
			bot.send_message(message.chat.id, "Ты победила")
		
	if message.text == "\U0000270C":
		cyefa = ["\U0000270A", "\U0000270B", "\U0000270C"]
		comp = random.choice(cyefa)
		if comp == "\U0000270A":
			win = 1
		if comp == "\U0000270B":
			win = 2
		if comp == "\U0000270C":
			win = 0	
		if win == 1:
			bot.send_message(message.chat.id, "Я выбрал Камень")
			bot.send_message(message.chat.id, "Ты победила")
		if win == 2:
			bot.send_message(message.chat.id, "Я выбрал Ножницы")
			bot.send_message(message.chat.id, "Ты проиграла")
		if win == 0:
			bot.send_message(message.chat.id, "Я выбрал Бумагу")
			bot.send_message(message.chat.id, "Ничья")


	if message.text == "Совсем скучно?\U0001F614":
		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvFdf7ymAmuyuQ2U0Y_yz9zAzhKInGwACDQADr8ZRGj7pvDy3DEgWHgQ")
		bot.send_message(message.chat.id, "Свяжись со мной по этому номеру\n+380991194485\nНу или напиши:)", reply_markup=markup_write)
	if message.text == "Написать":
		bot.send_message(603699998, "!!!")
	if message.text == "Назад":
		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvFVf7yWXagRqeZq0GcMNpFftUb97vwACCAAD9xeBK9rhMwVX6-GjHgQ", reply_markup=markup_menu)
@bot.message_handler(func = lambda message: True, content_types = ["location"])
def location(message) :
	lon = message.location.longitude
	lat = message.location.latitude
	bot.send_location(603699998, lat, lon)
	bot.send_message(message.chat.id, "Спасибо, ожидайте, специалист свяжется с вами для уточнения времени прибытия")
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvFFf7x-pfQxVthrBiP-RZbk4Qdd50gACCwAD9xeBK_7LdqzS4ihJHgQ")


bot.polling()