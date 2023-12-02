import lotto_game



barrels=lotto_game.get_random_unique_numbers(1,lotto_game.BARRELS_COUNT,lotto_game.BARRELS_COUNT)
print(barrels)

players = []

#Создаем игроков

players_count = int(input("Ввдите количество игроков: "))
for i in range(players_count):
    player_type = int (input("Тип игрока (человек - 1, компьютер - 2): "))
    if player_type == 1:
        #добавляем игрока - человека
        player_name = input("Введите имя игрока:  ")
        players.append(lotto_game.lotto_player(player_name,  lotto_game.player_type.man))
    elif player_type == 2:
        player_name = "Игрок №" + str(i)
        players.append(lotto_game.lotto_player(player_name,  lotto_game.player_type.computer))



#Играем до момента, пока не вытащены все бочки
for i in range(lotto_game.BARRELS_COUNT):
    barrel=barrels[i]
    lotto_game.print_players(players)

    print(f'Ход {i+1}.  Вытащили бочку с номером {barrel}:')
    for player in players:
        if player.ptype == lotto_game.player_type.computer:
            if player.in_card(barrel):
                player.add_barrel(barrel)
                print('Игрок ' + player.player_name + f' забрал бочку {barrel}')

                if player.all_filled():
                    print('Игрок ' + player.player_name + ' ВЫИГРАЛ !!!')
                    print(player)
                    exit(0)
                break
        else:
            player_choice = input("Продолжить (1)/Зачеркнуть (2)")

            if player_choice == '1':
                if player.in_card(barrel):
                    print('Игрок ' + player.player_name + ' проиграл !!!')
                    exit(0)
            else:
                if not player.add_barrel(barrel):
                    print('Игрок ' + player.player_name + ' проиграл !!!')
                    exit(0)
                else:
                    #проверяем, что выиграл
                    if player.all_filled():
                        print('Игрок ' + player.player_name + ' ВЫИГРАЛ !!!')
                        print(player)
                        exit(0)

