import random
from enum import Enum

BARRELS_COUNT = 90


def print_players(players):
    for p in players:
        print(p)


class player_type(Enum):
    man = 1
    computer = 2

    def __str__(self):
        if self.value == self.man:
            return 'человек'
        else:
            return 'компьютер'


def get_random_unique_numbers(min_num, max_num, count):
    ''' Генерим последовательность уникальных чисер в заданном диапазаоне
    :param min_num:
    :param max_num:
    :param count:
    :return:
    '''
    if min_num > max_num: return list([])

    l = list(range(min_num, max_num + 1))
    random.shuffle(l)
    return l[:count]


class lotto_player:
    """docstring"""

    _CARD_ROWS = 3
    _CARD_COLS = 9
    _NUMBERS_IN_ROW = 5


    def __init__(self,player_name, playertype):
        """Constructor"""
        self.barrels = list([])
        self.ptype = playertype
        self.create_player_card()
        self.player_name=player_name

    def create_player_card(self):
        self.card = []
        # Генерим пустое поле
        self.card = [[0] * self._CARD_COLS for i in range(self._CARD_ROWS)]

        # Все числа в карточке
        card_numbers = get_random_unique_numbers(1, BARRELS_COUNT, self._CARD_ROWS * self._NUMBERS_IN_ROW)

        # Идем по строкам
        for i in range(self._CARD_ROWS):
            # Индексы, где будут стоять числа в строке
            num_indexes = get_random_unique_numbers(0, self._CARD_COLS - 1, self._CARD_COLS - self._NUMBERS_IN_ROW + 1)
            num_indexes.sort()

            # Числа в строке
            row_numbers = card_numbers[i * self._NUMBERS_IN_ROW:(i + 1) * self._NUMBERS_IN_ROW]
            row_numbers.sort()

            # вставляем числа на места их индексов
            for j in range(self._NUMBERS_IN_ROW):
                self.card[i][num_indexes[j]] = row_numbers[j]

    def print_card(self):
        val = ''
        for i in range(self._CARD_ROWS):
            if i > 0:
                val += "\n"
            for j in range(self._CARD_COLS):
                if j > 0:
                    val += " "

                if self.card[i][j] == 0:
                    val += "  "
                elif self.card[i][j] == -1:
                    val += " -"
                else:
                    val += format(self.card[i][j], '2d')
        return val

    #Для удобства перегрузим оператор преобразования в строку
    def __str__(self):
        val = '-' * 30
        val += '\n Игрок ('
        val += str(self.ptype)
        val += '): ' + self.player_name + '\n'
        val += self.print_card()
        val += "\nБочки игрока"
        val += str(self.barrels)
        val += '\n'

        return val



    #добавим бочку в список у игрока
    def add_barrel(self, barrel):
        # Проверяем что бочка есть в карточке зачеркиваем ее и добавлем в список
        for i in range(self._CARD_ROWS):
            for j in range(self._CARD_COLS):
                if self.card[i][j] == barrel:
                    self.card[i][j] = -1
                    # Добавляем бочку в список
                    self.barrels.append(barrel)
                    return True
        return False

    #проверяем, что вся карточка заполнена
    def all_filled(self):

        print(len(self.barrels))
        print(self._CARD_ROWS*self._NUMBERS_IN_ROW)

        return len(self.barrels) == self._CARD_ROWS*self._NUMBERS_IN_ROW

    #Проверяем, что такое число у игрока есть

    def in_card(self, barrel):
        # Проверяем что бочка есть в карточке
        for i in range(self._CARD_ROWS):
            for j in range(self._CARD_COLS):
                if self.card[i][j] == barrel:
                    return True
        return False