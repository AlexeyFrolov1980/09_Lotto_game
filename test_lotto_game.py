import lotto_game
import unittest


class Test_lotto_game(unittest.TestCase):

    def setUp(self):
        self.player = lotto_game.lotto_player("Игрок 1", lotto_game.player_type.computer)

    def tearDown(self):
        del self.player

    #Тест проверки функции добавления бочки
    def test_add_barrel(self):

        # Находим номер, котрый есть в карточке
        b = 0
        for i in range(lotto_game.BARRELS_COUNT):
            if self.player.in_card(i):
                b = i
                break
        self.assertTrue(self.player.add_barrel(b))

        self.assertListEqual(self.player.barrels, [b])

        # Находим номер, котрого нет в карточке

        b = 0
        for i in range(lotto_game.BARRELS_COUNT):
            if not self.player.in_card(i):
                b = i
                break

        self.assertFalse(self.player.add_barrel(b))

    def test_in_card(self):
        #Проверяем что функция опредления наличия числа в карточке работает верно.
        for num_in_card in range(lotto_game.BARRELS_COUNT):

            is_in_card = False
            for i in range(self.player._CARD_ROWS):
                for j in range(self.player._CARD_COLS):
                    if self.player.card[i][j] == num_in_card:
                        is_in_card = True
                        break
                if is_in_card:
                    break

            if not is_in_card:
                self.assertFalse(self.player.in_card(num_in_card))
            else:
                self.assertTrue(self.player.in_card(num_in_card))

    def test_eq__(self):
        self.assertTrue(self.player == self.player)
        player1 = lotto_game.lotto_player("Тестовый игрок", lotto_game.player_type.man)
        self.assertFalse(self.player == player1)


    def test_ne__(self):
        self.assertFalse(self.player != self.player)
        player1 = lotto_game.lotto_player("Тестовый игрок", lotto_game.player_type.man)
        self.assertTrue(self.player != player1)


