import pytest

from gamesdb_api.gamesdb_api import GamesDB
from gamesdb_api.gamesdb_api import URL_CONSOLES


class TestClass:

    def test_get_game_by_id_quando_passado_argumento_que_nao_eh_str_ou_lista_com_str_retorna_erro(self):
        with pytest.raises(Exception):
            entrada = 100
            resultado = GamesDB().get_game_by_id(entrada)

            assert resultado

    def test_get_game_by_id_quando_passado_argumento_que_nao_eh_str_ou_lista_com_str_retorna_False(self):
        entrada = 100
        esperado = False

        resultado = GamesDB().get_game_by_id(entrada)

        assert resultado == esperado

    def test_get_game_by_id_quando_passado_argumento_que_eh_uma_lista_e_tem_valores_que_nao_eh_str_retorna_Erro(self):
        with pytest.raises(Exception):
            entrada = ['2', 1, '12']
            resultado = GamesDB().get_game_by_id(entrada)

            assert resultado

    def test_get_game_by_id_quando_passado_argumento_que_eh_uma_lista_e_tem_valores_que_nao_eh_str_retorna_False(self):
        entrada = [100]
        esperado = False

        resultado = GamesDB().get_game_by_id(entrada)

        assert resultado == esperado

    def test_get_game_by_name_quando_passado_argumento_que_nao_eh_str_ou_lista_com_str_retorna_erro(self):
        with pytest.raises(Exception):
            entrada = 100
            resultado = GamesDB().get_game_by_name(entrada, 6)

            assert resultado

    def test_get_game_by_name_quando_passado_argumento_que_nao_eh_str_ou_lista_com_str_retorna_False(self):
        entrada = 100
        esperado = False

        resultado = GamesDB().get_game_by_name(entrada, 'Super Nintendo (SNES)')

        assert resultado == esperado

    def test_get_game_by_name_quando_passado_argumento_que_eh_uma_lista_e_tem_valores_que_nao_eh_str_retorna_Erro(self):
        with pytest.raises(Exception):
            entrada = ['super mario world', 1, 'Super Bomberman 4']
            resultado = GamesDB().get_game_by_name(entrada, 6)

            assert resultado

    def test_get_game_by_name_quando_passado_argumento_que_eh_uma_lista_e_tem_valores_que_nao_eh_str_retorna_False(
            self):
        entrada = [100]
        esperado = False

        resultado = GamesDB().get_game_by_name(entrada, 6)

        assert resultado == esperado

    def test_clear_name_quando_recebe_Game_The_o_jogo_retorna_The_game_o_jogo(self):
        entrada = 'Game, The - O jogo'
        esperado = 'the+game+o+jogo'

        resultado = GamesDB()._GamesDB__clear_name(entrada)

        assert resultado == esperado

    def test_get_consoles_retorna_um_dict(self):

        resultado = GamesDB()._GamesDB__get_consoles(URL_CONSOLES)

        assert isinstance(resultado, dict)

    def test_get_game_by_id_quando_passado_o_str_100_retorna_uma_lista_com_uma_dict_com_title_igual_a_spider_man_3(self):
        entrada = '100'
        esperado = 'Spider-Man 3'

        resultado = GamesDB().get_game_by_id(entrada)['game_title']

        assert resultado == esperado

    def test_get_game_by_id_quando_passado_um_id_de_um_jogo_nao_existente_retorna_list_dict_com_not_found_i(self):
        entrada = "10000"
        esperado = {'not_found': '10000'}

        resultado = GamesDB().get_game_by_id(entrada)

        assert resultado == esperado

    def test_scrapping_game_quando_passado_o_int_10000_pagina_do_jogo_nao_existe_retorna_false(self):
        entrada = '10000'
        esperado = False

        resultado = GamesDB()._GamesDB__scraping_game(entrada)

        assert resultado == esperado

    def test_get_game_by_id_quando_passado_uma_lista_com_valores_100_e_101_retorna_uma_lista_com_tamanho_2(self):
        entrada = ['100', '101']
        esperado = 2

        resultado = len(GamesDB().get_game_by_id(entrada))

        assert resultado == esperado

    def test_busca_recebe_lista_e_um_o_termo_Aero_the_Acro_Bat_retorna_1527(self):
        entrada = 'Aero the Acro-Bat'
        esperado = 1527

        resultado = GamesDB()._GamesDB__busca({1520: 'Batman', 1527: 'Aero the Acro-Bat'}, entrada)

        assert resultado == esperado

    def test_get_game_by_name_recebe_uma_lista_de_str_retorna_uma_lista(self):
        entrada = ['Aero the Acro-Bat', 'Air Cavalry', 'adfkoie']
        esperado = type(entrada)

        resultado = type(GamesDB().get_game_by_name(entrada, 'Super Nintendo (SNES)'))

        assert resultado == esperado

    def test_get_game_by_name_recebe_uma_str_retorna_uma_lista(self):
        entrada = 'Air Cavalry'
        esperado = type({})

        resultado = type(GamesDB().get_game_by_name(entrada, 'Super Nintendo (SNES)'))

        assert resultado == esperado