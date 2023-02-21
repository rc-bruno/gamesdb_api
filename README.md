# Sobre GamesDB

GamesDB é uma classe Python que permite a busca de informações sobre jogos eletrônicos em um site com o mesmo nome. A classe usa as bibliotecas BeautifulSoup, requests e fuzzywuzzy.

A classe tem um método de busca de jogo pela identificação dele no site e um método busca por nome. Ambos retornam uma lista com um dicionário para cada jogo procurado ou apenas um dicionário se apenas um jogo for procurado. As seguintes informações do jogo são retornadas:

- id
- game_title
- overview
- genres
- esrb_rating
- trailer
- platform
- region
- developers
- publishers
- release_date
- players
- coop
- cover
- cover_thumb
- fanarts
- screenshots
- clearlogos

A classe tem um método de busca de console pela identificação dele no site e um método busca por nome. Ambos retornam uma dicionário com informações do jogo procurado. As seguintes informações do jogo são retornadas:

- id
- name
- overview
- developer
##Instalando
    pip install gamesdb-api

## Como usar

    >>> from gamesdb_api import GamesDB
    >>> gdb = GamesDB()
    
### Busca de jogo por identificador:
Passa como parâmetro uma id e retorna um dicionário com informações de um jogo

    >>> games = gbd.get_game_by_id('5')
    >>> print(games)

    {'id': '5', 'game_title': 'Donkey Kong', 'overview': "Can you save Mario's girl from the clutches of Donkey Kong? Donkey Kong has kidnapped Mario's girlfriend Pauline and taken her to the top of a construction site. It's up to you to help Mario save Pauline before time runs out. But it won't be easy. Donkey Kong will do everything in his power to stop you. He'll throw barrel bombs, flaming fireballs and anything else he can get his hands on. So if you're looking for action, don't monkey around. Get the original Donkey Kong from the Nintendo Arcade Classics Series!", 'platform': 'Nintendo Entertainment System (NES)', 'region': 'NTSC-U', 'developers': ['Nintendo R&D2'], 'publishers': ['Nintendo'], 'release_date': '1986-06-01', 'players': '2', 'coop': 'No', 'trailer': 'https://youtube.com/watch?v=C_PrG8P5W8o', 'esrb_rating': 'E - Everyone', 'genres': ['Platform'], 'cover': 'https://cdn.thegamesdb.net/images/original/boxart/front/5-2.jpg', 'cover_thumb': None, 'fanarts': ['https://cdn.thegamesdb.net/images/original/fanart/5-4.jpg', 'https://cdn.thegamesdb.net/images/original/fanart/5-1.jpg'], 'screenshots': ['https://cdn.thegamesdb.net/images/original/screenshots/5-1.jpg'], 'clearlogos': ['https://cdn.thegamesdb.net/images/original/clearlogo/5.png']}
 
Passa como parâmetro uma lista com ids e retorna uma lista com um dicionário para jogo pesquisado.

    >>> lista = ['5','23','100']
    >>> games = gdb.get_game_by_id(lista)
    >>> for game in games:
    >>>     print (games)

    {'id': '5', 'game_title': 'Donkey Kong', 'overview': "Can you save Mario's girl from the clutches of Donkey Kong? Donkey Kong has kidnapped Mario's girlfriend Pauline and taken her to the top of a construction site. It's up to you to help Mario save Pauline before time runs out. But it won't be easy. Donkey Kong will do everything in his power to stop you. He'll throw barrel bombs, flaming fireballs and anything else he can get his hands on. So if you're looking for action, don't monkey around. Get the original Donkey Kong from the Nintendo Arcade Classics Series!", 'platform': 'Nintendo Entertainment System (NES)', 'region': 'NTSC-U', 'developers': ['Nintendo R&D2'], 'publishers': ['Nintendo'], 'release_date': '1986-06-01', 'players': '2', 'coop': 'No', 'trailer': 'https://youtube.com/watch?v=C_PrG8P5W8o', 'esrb_rating': 'E - Everyone', 'genres': ['Platform'], 'cover': 'https://cdn.thegamesdb.net/images/original/boxart/front/5-2.jpg', 'cover_thumb': None, 'fanarts': ['https://cdn.thegamesdb.net/images/original/fanart/5-4.jpg', 'https://cdn.thegamesdb.net/images/original/fanart/5-1.jpg'], 'screenshots': ['https://cdn.thegamesdb.net/images/original/screenshots/5-1.jpg'], 'clearlogos': ['https://cdn.thegamesdb.net/images/original/clearlogo/5.png']}
    {'id': '23', 'game_title': 'Gears of War', 'overview': 'The game focuses on the troops of Delta Squad as they fight to save the human inhabitants of the fictional planet Sera from a relentless subterranean enemy known as the Locust Horde. The player assumes the role of Marcus Fenix, a former prisoner and war-hardened soldier. The game is based on the use of cover and strategic fire for the player to advance through the scenarios; a second player can play cooperatively through the main campaign to assist. The game also features several online multiplayer game modes for up to eight players.', 'platform': 'PC', 'region': 'Region Not Set', 'developers': ['Epic'], 'publishers': ['Microsoft Studios'], 'release_date': '2006-11-07', 'players': '2', 'coop': 'Yes', 'trailer': 'https://youtube.com/watch?v=_D9r8Xm2aDw', 'esrb_rating': 'M - Mature 17+', 'genres': ['Shooter'], 'cover': 'https://cdn.thegamesdb.net/images/original/boxart/front/23-1.jpg', 'cover_thumb': None, 'fanarts': ['https://cdn.thegamesdb.net/images/original/fanart/23-1.jpg', 'https://cdn.thegamesdb.net/images/original/fanart/23-2.jpg'], 'screenshots': ['https://cdn.thegamesdb.net/images/original/screenshots/23-1.jpg'], 'clearlogos': []}
    {'id': '100', 'game_title': 'Spider-Man 3', 'overview': "The game's plot expands on the film by including additional characters and elements from the Spider-Man comics and the Marvel Universe. Depending on the platform, different villains from the comics are featured, but all versions of the game feature the film's main villains: Venom, New Goblin, and Sandman.", 'platform': 'Sony Playstation 3', 'region': 'Region Not Set', 'developers': ['Treyarch'], 'publishers': ['Activision'], 'release_date': '2007-05-04', 'players': '1', 'coop': 'No', 'trailer': 'https://youtube.com/watch?v=O4JB4B4RXpg', 'esrb_rating': 'T - Teen', 'genres': ['Action'], 'cover': 'https://cdn.thegamesdb.net/images/original/boxart/front/100-1.jpg', 'cover_thumb': None, 'fanarts': ['https://cdn.thegamesdb.net/images/original/fanart/100-1.jpg', 'https://cdn.thegamesdb.net/images/original/fanart/100-2.jpg', 'https://cdn.thegamesdb.net/images/original/fanart/100-3.jpg', 'https://cdn.thegamesdb.net/images/original/fanart/100-4.jpg'], 'screenshots': ['https://cdn.thegamesdb.net/images/original/screenshots/100-1.jpg'], 'clearlogos': ['https://cdn.thegamesdb.net/images/original/clearlogo/100.png']}
    



### Busca de jogo por nome:
Passa como parâmetro um nome e retorna um dicionário.

    >>> games = gdb.get_game_by_name('Super Mario World', 'Super Nintendo (SNES)')
    ou
    >>> games = gdb.get_game_by_name('Super Mario Word', 6)

    {'id': '83376', 'game_title': 'Super Mario World', 'overview': 'No overview is currently available for this title, please feel free to add one.', 'platform': 'Super Nintendo (SNES)', 'region': 'NTSC-J', 'developers': ['Nintendo'], 'publishers': ['Nintendo'], 'release_date': '1990-11-21', 'players': '2', 'coop': 'No', 'esrb_rating': 'E - Everyone', 'genres': ['Platform'], 'cover': 'https://cdn.thegamesdb.net/images/original/boxart/front/83376-1.jpg', 'cover_thumb': None, 'fanarts': [], 'screenshots': [], 'clearlogos': []}
Passa como parâmetro um lista com nomes e retorna uma lista com dicionários.

    >>> lista = ['Super Mario World','Jogo Qualquer','Final Fantasy 3']
    >>> games = gdb.get_game_by_name(lista, 'Super Nintendo (SNES)')
    ou
    >>> games = gdb.get_game_by_name(lista, 6')
    >>> for game in games:
    >>>     print(game)    

    {'id': '83376', 'game_title': 'Super Mario World', 'overview': 'No overview is currently available for this title, please feel free to add one.', 'platform': 'Super Nintendo (SNES)', 'region': 'NTSC-J', 'developers': ['Nintendo'], 'publishers': ['Nintendo'], 'release_date': '1990-11-21', 'players': '2', 'coop': 'No', 'esrb_rating': 'E - Everyone', 'genres': ['Platform'], 'cover': 'https://cdn.thegamesdb.net/images/original/boxart/front/83376-1.jpg', 'cover_thumb': None, 'fanarts': [], 'screenshots': [], 'clearlogos': []}
    {'not_found': 'Jogo Qualquer'}
    {'id': '1762', 'game_title': 'Final Fantasy V', 'overview': "The Elemental Crystals...the life source of the planet. With them, gentle winds blow, the seas are active, fire burns bright, and the earth is full of life. All seems well in the world, until the wind suddenly stops, the sea begin to grow stagnant, the heat of fire becomes scarce, and the earth begins to wither. King Tycoon, sensing a premonition of evil, hurries off to check on the Wind Crystal, only to witness it destroy itself.\r\n\r\nMeanwhile, a young traveler named Butz is camping in a field when a giant meteor strikes the planet. When he heads out to examine the meteor, he is shocked to find a young girl named Lenna, who is the princess of Tycoon, and a old man named Galuf, who is on a critical mission. Later, joined by Faris, a pirate captain, the foursome must travel the land in search of the destructor of the Crystals, and save the planet at any cost!\r\n\r\nFinal Fantasy V featured many new gameplay options and tactics, including an improved Job/Ability system (like in Final Fantasy Tactics), the return of the ATB (Active Time Battle) turn system, and all of the classic FF gameplay you've come to know and love!\r\n\r\nFinal Fantasy V was released as a stand-alone game in Japan, and again in Final Fantasy Collection. Its U.S. debut was as part of Final Fantasy Anthology. It was also later ported to the Gameboy Advance, adding 4 new Jobs, a new 30-floor dungeon, a bestiary, a music player, the ability to quick save anywhere, a few extra pieces of equipment, and a newly update translation.", 'platform': 'Super Nintendo (SNES)', 'region': 'Region Not Set', 'developers': ['Squaresoft'], 'publishers': ['Squaresoft'], 'release_date': '1992-12-06', 'players': '1', 'coop': 'No', 'genres': ['Role-Playing'], 'cover': 'https://cdn.thegamesdb.net/images/original/boxart/front/1762-2.jpg', 'cover_thumb': None, 'fanarts': ['https://cdn.thegamesdb.net/images/original/fanart/1762-1.jpg', 'https://cdn.thegamesdb.net/images/original/fanart/1762-2.jpg', 'https://cdn.thegamesdb.net/images/original/fanart/1762-3.jpg', 'https://cdn.thegamesdb.net/images/original/fanart/1762-4.jpg', 'https://cdn.thegamesdb.net/images/original/fanart/1762-5.jpg'], 'screenshots': [], 'clearlogos': ['https://cdn.thegamesdb.net/images/original/clearlogo/1762.png']}


### Nomes e códigos de consoles:

    >>> for name, id in gbd.codigo_console.items():
    >>> print(f'{name}-{id}

### Busca de console por identificador

Passa um id como parâmetro e retorna um dicionário com informações do console.

    >>> console = gdb.get_console_by_id(12)
    >>> print(console)
    {'id': '12', 'name': 'Sony Playstation 3', 'overview': "The PlayStation 3, (officially abbreviated as PS3) is the third home video game console produced by Sony Computer Entertainment and the successor to the PlayStation 2 as part of the PlayStation series.\r\n\r\nThe PlayStation 3 competes with Microsoft's Xbox 360 and Nintendo's Wii as part of the seventh generation of video game consoles. It was first released on November 11, 2006, in Japan, with international markets following shortly thereafter.", 'developer': 'Sony'}

Passa um nome como paràmetro e retorna um dicionário com informações do console.

    >>> console = gdb.get_console_by_name('Sony Playstation 3')
    >>> print(console)
    {'id': '12', 'name': 'Sony Playstation 3', 'overview': "The PlayStation 3, (officially abbreviated as PS3) is the third home video game console produced by Sony Computer Entertainment and the successor to the PlayStation 2 as part of the PlayStation series.\r\n\r\nThe PlayStation 3 competes with Microsoft's Xbox 360 and Nintendo's Wii as part of the seventh generation of video game consoles. It was first released on November 11, 2006, in Japan, with international markets following shortly thereafter.", 'developer': 'Sony'}
