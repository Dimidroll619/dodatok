import telebot
from telebot import types
import random



bot = telebot.TeleBot("1417831455:AAEXoPuUxO69Djha87hHQK09qjUnt0iWsAM") #токен
#клавиатура
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
markup_write = types.ReplyKeyboardMarkup(resize_keyboard = True,  row_width = 1)
markup_game = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
markup_ggame = types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 1)
btn_music = types.KeyboardButton ("Послухаєм музику?\U0001F3A7")
btn_game = types.KeyboardButton ("Поиграем?\U0001F3AE")
btn_help = types.KeyboardButton ("Нажми\U0001F448")
btn_back = types.KeyboardButton ("Назад")
btn_rock = types.KeyboardButton ("\U0000270A")
btn_scissors = types.KeyboardButton ("\U0000270B")
btn_papper = types.KeyboardButton ("\U0000270C")
markup_menu.add(btn_music, btn_game, btn_help)
markup_write.add(btn_back)
markup_game.add(btn_rock, btn_scissors, btn_papper, btn_back)


@bot.message_handler(commands=['start',])
def send_welcome(message):
	first_name = message.chat.first_name #Ім`я
	last_name = str(message.chat.last_name) #Прізвище
	bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvAhf7ijAAh3PymbLbclu_lbhVmmDyQACBQAD9xeBK95mq4g2GUDbHgQ")
	bot.send_message(message.chat.id, "Привіт, " + first_name +" "+ last_name + "! \nМене звати Федька, я створений шоб тебе здивувати \nНаразі попробуєм трошки повеселитись, а якщо тобі сподобається то мій інтерфейс буде розширено", reply_markup=markup_menu)

@bot.message_handler(content_types = ["text"])
def message(message):
	if message.text == "Послухаєм музику?\U0001F3A7":
		dir3 = ["https://su.muzmo.cc/get/music/20201210/Klava_Koka_-_Pyanuyu_domojj_71911012.mp3",
		"https://su.muzmo.cc/get/music/20201230/MORGENSHTERN_-_Cristal_MOJOT_72141222.mp3",
		"https://su.muzmo.cc/get/music/20201128/KHABIB_-_YAgoda_malinka_71770520.mp3",
		"https://su.muzmo.cc/get/music/20201212/NILETTO_-_nevyvoZIMAya_71937924.mp3",
		"https://su.muzmo.cc/get/music/20201219/Big_Baby_Tape_-_KARI_72019832.mp3",
		"https://su.muzmo.cc/get/music/20201216/Gazan_-_ABU_BANDIT_71984240.mp3",
		"https://su.muzmo.cc/get/music/20201024/Karol_G_-_BICHOTA_71364501.mp3",
		"https://su.muzmo.cc/get/music/20190416/Rosala_J_Balvin_El_Guincho_-_Con_Altura_63547717.mp3",
		"https://su.muzmo.cc/get/music/20201212/Ramil_-_Aromat_71933540.mp3",
		"https://su.muzmo.cc/get/music/20201220/Kangi_-_JEjjya_72034273.mp3",
		"https://su.muzmo.cc/get/music/20200829/BLACKPINK_Selena_Gomez_-_Ice_Cream_70746192.mp3",
		"https://su.muzmo.cc/get/music/20201210/Mia_Boyka_-_AU_71911020.mp3",
		"https://su.muzmo.cc/get/music/20201212/Ramil_-_Sigaretnyjj_dym_71933543.mp3",
		"https://su.muzmo.cc/get/music/20201216/Egor_Krid_-_Ty_ne_smogla_prostit_71984253.mp3",
		"https://su.muzmo.cc/get/music/20201204/_-_Phut_Hon_71837654.mp3",
		"https://su.muzmo.cc/get/music/20201208/ANIVAR_-_Kaplya_kisloroda_71885448.mp3",
		"https://su.muzmo.cc/get/music/20190521/Karol_G_-_Ocean_64380665.mp3",
		"https://su.muzmo.cc/get/music/20201216/Anet_Sajj_-_Ne_revi_71984238.mp3",
		"https://su.muzmo.cc/get/music/20200530/Lady_Gaga_BLACKPINK_-_Sour_Candy_69739914.mp3",
		"https://su.muzmo.cc/get/music/20201209/VESNA305_-_Novyjj_god_71900183.mp3",
		"https://su.muzmo.cc/get/music/20201002/Foushe_-_Deep_End_71122114.mp3",
		"https://su.muzmo.cc/get/music/20201214/GUDZON_-_Novyjj_god_71961949.mp3",
		"https://su.muzmo.cc/get/music/20201212/Rauf_Faik_Toxi_-_TEBYA_NET_SO_MNOJJ_71937947.mp3",
		"https://su.muzmo.cc/get/music/20180420/Natti_Natasha_Becky_G_-_Sin_Pijama_55405694.mp3",
		"https://su.muzmo.cc/get/music/20201226/Miyagi_Andy_Panda_-_All_the_Time_72097453.mp3",
		"https://su.muzmo.cc/get/music/20201215/Idris_Leos_-_V_poslednijj_raz_71972489.mp3",
		"https://su.muzmo.cc/get/music/20201212/Polina_Gagarina_-_ZIMA_71937923.mp3",
		"https://su.muzmo.cc/get/music/20170830/Viktor_Cojj_-_Gruppa_krovi_47828908.mp3",
		"https://su.muzmo.cc/get/music/20201208/ANIVAR_-_Kaplya_kisloroda_71885448.mp3",
		"https://su.muzmo.cc/get/music/20190521/Karol_G_-_Ocean_64380665.mp3",
		"https://su.muzmo.cc/get/music/20201002/Foushe_-_Deep_End_71122114.mp3"]
		mus = random.choice(dir3)
		bot.send_document(message.from_user.id, mus)	


	if message.text == "Поиграем?\U0001F3AE":
		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvdRf818dGfnlvYLCwfPcSPUaOo8-igACgQMAAm2wQgOxqAABZxcolQABHgQ")
		bot.send_message(message.chat.id, "Будем грати в \"камінь, ножиці, папір\"", reply_markup=markup_game)
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
			bot.send_message(message.chat.id, "Я вибрав Камінь")
			bot.send_message(message.chat.id, "Нічия")
		if win == 1:
			bot.send_message(message.chat.id, "Я вибрав Ножиці")
			bot.send_message(message.chat.id, "Ти перемогла")
		if win == 2:
			bot.send_message(message.chat.id, "Я вибрав Папір")
			bot.send_message(message.chat.id, "Ти програла")

	if message.text == "\U0000270B":
		cyefa = ["\U0000270A", "\U0000270B", "\U0000270C"]
		comp = random.choice(cyefa)
		if comp == "\U0000270A":
			win = 1
		if comp == "\U0000270B":
			win = 0
		if comp == "\U0000270C":
			win = 2
		if win == 1:
			bot.send_message(message.chat.id, "Я вибрав Камінь")
			bot.send_message(message.chat.id, "Ти перемогла")
		if win == 0:
			bot.send_message(message.chat.id, "Я вибрав Папір")
			bot.send_message(message.chat.id, "Нічия")
		if win == 2:
			bot.send_message(message.chat.id, "Я вибрав Ножиці")
			bot.send_message(message.chat.id, "Ти програла")
		
	if message.text == "\U0000270C":
		cyefa = ["\U0000270A", "\U0000270B", "\U0000270C"]
		comp = random.choice(cyefa)
		if comp == "\U0000270A":
			win = 2
		if comp == "\U0000270B":
			win = 1
		if comp == "\U0000270C":
			win = 0	
		if win == 1:
			bot.send_message(message.chat.id, "Я вибрав Камінь")
			bot.send_message(message.chat.id, "Ти програла")
		if win == 2:
			bot.send_message(message.chat.id, "Я вибрав Папір")
			bot.send_message(message.chat.id, "Ти перемогла")
		if win == 0:
			bot.send_message(message.chat.id, "Я вибрав Ножиці")
			bot.send_message(message.chat.id, "Нічия")


	if message.text == "Нажми\U0001F448":
		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvFdf7ymAmuyuQ2U0Y_yz9zAzhKInGwACDQADr8ZRGj7pvDy3DEgWHgQ")
		bot.send_message(603699998, "!!!")
		bot.send_message(message.chat.id, "Надіюсь я тебе здивував і ти нарешті розповіси те що маєш. Швидше за все я знаю, шо ти хочеш сказати, але сумніви є, тому я слухаю", reply_markup=markup_write)
		
	if message.text == "Назад":
		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvFVf7yWXagRqeZq0GcMNpFftUb97vwACCAAD9xeBK9rhMwVX6-GjHgQ", reply_markup=markup_menu)



bot.polling()