from typing import Union, List, Any

URL_PESQUISA = 'https://thegamesdb.net/search.php?name=<search>&platform_id%5B%5D=<id>'
URL_GAME_ID = 'https://thegamesdb.net/game.php?id=<id>'
URL_CONSOLES = 'https://thegamesdb.net/list_platforms.php'
URL_CONSOLE_ID = "https://thegamesdb.net/platform.php?id=<id>"
TYPE_GAME = dict[str, Union[str, Union[List[str], str]]]
