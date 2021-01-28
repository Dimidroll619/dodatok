import telebot
from telebot import types
import random



bot = telebot.TeleBot("1646880221:AAHGY14vQ6zKdUt-DeYu70L0A4lPr8Adepk") #токен
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
btn_rock = types.KeyboardButton ("\U0000270A")
btn_scissors = types.KeyboardButton ("\U0000270B")
btn_papper = types.KeyboardButton ("\U0000270C")
btn_ggame = types.KeyboardButton ("/game")
markup_menu.add(btn_film, btn_music, btn_game, btn_help, btn_sos)
markup_film.add(btn_vidomi, btn_nevidomi, btn_back)
markup_write.add(btn_back)
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
		"https://images.1plus1.video/playlist-1/103018/81b4583d8a63beeba75530292fdd2261.768x576.jpg",
		"https://upload.wikimedia.org/wikipedia/ru/d/d3/%D0%9F%D0%BE%D0%BB%D0%B8%D1%86%D0%B5%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D1%81_%D0%A0%D1%83%D0%B1%D0%BB%D1%91%D0%B2%D0%BA%D0%B8.jpg",
		"https://upload.wikimedia.org/wikipedia/ru/f/f4/%D0%A1%D0%B5%D1%80%D0%B8%D0%B0%D0%BB_%D0%9A%D1%83%D1%85%D0%BD%D1%8F.jpg",
		"https://img.tvdate.ru/serials/svetofor/svetofor-big-poster.jpg",
		"https://upload.wikimedia.org/wikipedia/ru/6/69/%D0%9B%D0%BE%D0%B3%D0%BE%D1%82%D0%B8%D0%BF_%D1%82%D0%B5%D0%BB%D0%B5%D1%81%D0%B5%D1%80%D0%B8%D0%B0%D0%BB%D0%B0_%D0%A1%D1%87%D0%B0%D1%81%D1%82%D0%BB%D0%B8%D0%B2%D1%8B_%D0%B2%D0%BC%D0%B5%D1%81%D1%82%D0%B5.jpg",
		"https://img.tvdate.ru/serials/svetofor/svetofor-big-poster.jpg",
		"https://www.kino-teatr.ru/movie/posters/big/6/85166.jpg",
		"https://s3.cdn.teleprogramma.pro/wp-content/uploads/2018/03/6997a79718624372fb2b52b526911227.jpg",
		"https://static.hdrezka.ac/i/2018/3/22/cda6382a64a03fr21t40g.jpg",
		"https://upload.wikimedia.org/wikipedia/ru/d/d2/Zaitsevplus1.jpg",
		"https://upload.wikimedia.org/wikipedia/ru/c/c9/Vosmidesyatye-poster.jpg"]
		film1 = random.choice(dir1)
		bot.send_photo(message.from_user.id, film1)
	if message.text == "Рекомендации\U0001F50D":
		dir2 = ["https://funkyimg.com/u2/2703/003/239277-Sherlock-Holmes-2009.jpg", 
		"https://www.themoviedb.org/t/p/original/5ETeBL0ybRW5D4hy2lARo3q7iH2.jpg", 
		"https://upload.wikimedia.org/wikipedia/ru/8/8a/We%27re_the_Millers.jpeg",
		"https://upload.wikimedia.org/wikipedia/ru/3/39/The_Bounty_Hunter.jpg",
		"https://www.film.ru/sites/default/files/movies/posters/Vacation-2624174.jpg",
		"https://www.veseloeradio.ru/design/images/actions/2016/dedushka/cover.jpg",
		"https://upload.wikimedia.org/wikipedia/ru/b/b9/Intouchables.jpg",
		"https://u.kanobu.ru/longreads/2020/6/6/e8f38718-8c84-4c48-856a-ca6baec3aade.jpg",
		"https://upload.wikimedia.org/wikipedia/ru/3/3a/About_Time.jpg",
		"https://thumbs.dfs.ivi.ru/storage3/contents/d/f/0b0e71bba483d0510c3c9750c7240b.jpg",
		"https://www.kinopoisk.ru/images/film_big/391772.jpg",
		"https://thumbs.dfs.ivi.ru/storage8/contents/6/e/9a7512dd1f3f449ddce40a6c37da34.jpg",
		"https://st.kp.yandex.net/images/film_iphone/iphone360_1009784.jpg",
		"https://st.kp.yandex.net/images/film_iphone/iphone360_195524.jpg",
		"https://upload.wikimedia.org/wikipedia/ru/5/50/I_robot_2004_poster1.jpg",
		"https://static.hdrezka.ac/i/2014/12/19/ca0aeaf80af0bkr53y32n.jpg",
		"https://b1.filmpro.ru/c/438209.246x347.jpg",
		"https://s3.vcdn.biz/static/f/272583561/image.jpg",
		"https://www.kinopoisk.ru/images/film_big/602677.jpg"]
		film2 = random.choice(dir2)
		bot.send_photo(message.from_user.id, film2)	
		
	if message.text == "Послушать музыку\U0001F3A7":
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
			win = 1
		if comp == "\U0000270B":
			win = 0
		if comp == "\U0000270C":
			win = 2
		if win == 1:
			bot.send_message(message.chat.id, "Я выбрал Камень")
			bot.send_message(message.chat.id, "Ти победила")
		if win == 0:
			bot.send_message(message.chat.id, "Я выбрал Бумагу")
			bot.send_message(message.chat.id, "Ничья")
		if win == 2:
			bot.send_message(message.chat.id, "Я выбрал Ножницы")
			bot.send_message(message.chat.id, "Ти проиграла")
		
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
			bot.send_message(message.chat.id, "Я выбрал Камень")
			bot.send_message(message.chat.id, "Ти проиграла")
		if win == 2:
			bot.send_message(message.chat.id, "Я выбрал Бумагу")
			bot.send_message(message.chat.id, "Ти победила")
		if win == 0:
			bot.send_message(message.chat.id, "Я выбрал Ножницы")
			bot.send_message(message.chat.id, "Ничья")


	if message.text == "Совсем скучно?\U0001F614":
		bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEBvFdf7ymAmuyuQ2U0Y_yz9zAzhKInGwACDQADr8ZRGj7pvDy3DEgWHgQ")
		bot.send_message(603699998, "!!!")
		bot.send_message(message.chat.id, "Свяжись со мной по этому номеру\n+380991194485\nНу или напиши:)", reply_markup=markup_write)
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