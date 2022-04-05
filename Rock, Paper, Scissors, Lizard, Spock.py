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
rock = ('rock')
paper = ('paper')
scissors = ('scissors')
lizard = ('lizard')
spock = ('spock')

rock > scissors, lizard, spock

def out():
    quit()


def inp():
    player_1 = input(f'{player} ')
    if player_1 not in spisok:
        print (f'{inval} "{player_1}"')
        wrong()
    else:
        return player_1


def wrong():
    rep = input(f'{repeat} ')
    if rep in yes:
        winner()
    if rep in no:
        out()
    else:
        print (f'{inval} "{rep}"')
        wrong()


def rand():
    computer = random.choice(spisok)
    return computer


def winner():
    comp_1 = rand()
    player_2 = inp()
    if player_2 == 'rock' and comp_1 == 'paper':
        print(comp)
    if player_2 == 'paper' and comp_1 == 'rock':
        print(play)
    #else:
        #print (f'{player_2} {comp_1} {draw}')
    winner()


winner()




