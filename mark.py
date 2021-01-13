
institutet = [{
    "title" : "hfd",
    "lonm": 49.804128,
    "latm": 24.066063,
    "adress" : "zelena vyl"
 },{
    "title" : "h2",
    "lonm": 43.804128,
    "latm": 22.066063,
    "adress" : "zelena vy11"
}
]

	all_files_in_directory = os.listdir(path = "D:/Python/film1")
		file = random.choice(all_files_in_directory)
		doc = open("D:/Python/film1"+"/"+file, "rb")
		caption = "123"
		bot.send_photo(chat_id, doc, caption)
