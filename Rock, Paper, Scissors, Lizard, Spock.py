import random

player = ('Your choice (rock paper scissors lizard spock?) ')
spisok = ('rock', 'paper', 'scissors', 'lizard', 'spock')
comp = ('Computer WIN!')
play = ('Player WIN')
draw = ('No one WIN')
repeat = ('Repeat (Y/N)?')
inval = ('Invalid input')
yes = ('y', 'Y')
no = ('n', 'N')


    #выход

def out():
    quit()


    #проверка входящих данных

def inp():
    player_1 = input(f'{player} ')
    if player_1 not in spisok:
        print (f'{inval} "{player_1}"')
        wrong()
    else:
        return player_1


    #запрос на повторный ввод

def wrong():
    rep = input(f'{repeat} ')
    if rep in yes:
        winner()
    if rep in no:
        out()
    else:
        print (f'{inval} "{rep}"')
        wrong()

    #выбор роли компьютера

def rand():
    computer = random.choice(spisok)
    return computer


    #выбор победителя

def winner():
    comp_1 = rand()
    player_2 = inp()
    print(player_2)
    print(comp_1)
    rock_1 = ('scissors', 'lizard')
    paper_1 = ('rock', 'spock')
    scissors_1 = ('paper', 'lizard')
    lizard_1 = ('spock', 'paper')
    spock_1 = ('scissors', 'rock')
    if player_2 == 'rock' and comp_1 in rock_1:
        print(play)
    elif player_2 == 'paper' and comp_1 in paper_1:
        print(play)
    elif player_2 == 'scissors' and comp_1 in scissors_1:
        print (play)
    elif player_2 == 'lizard' and comp_1 in lizard_1:
        print (play)
    elif player_2 == 'spock' and comp_1 in spock_1:
        print (play)
    elif player_2 == comp_1:
        print (f'{player_2} {comp_1} {draw}')
    else:
        print (comp)

    wrong()


winner()

