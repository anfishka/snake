
# С использованием функций
# Написать игру
# Суть в том, что появляется игровое поле 10 на 10 символов заполненное внутри пробелом, а внешне - *
# Появляется игрок в виде символа @
# Появляется враги в виде символа + (с каждым уровнем +1 )
# Суть игры в том, чтобы за минимальное количество шагов сьесть всех врагов
# Изначально есть 5 ходов
# За каждого враша +5 ходов
# Враги появляются по случайным координатам
#
import random

BATTLEFIELD = []
BATTLEFIELD_SIZE = 10
EMPTY = ' '
STAR = '*'
PLAYER = '@'
ENEMY = '+'
STEPS = 5
TOTAL_ENEMIES = 2
NEEDS_TO_KILL_TOTAL_ENEMIES = TOTAL_ENEMIES
DEFEATED_ENEMIES = 0
LEVEL = 0
DIRECTIONS = ['W','S','D','A']
CURRENT_PLAYER_POS_H = 0
CURRENT_PLAYER_POS_V = 0

def createBattleField():
    for i in range(BATTLEFIELD_SIZE):
        tmp = []
        for j in range(BATTLEFIELD_SIZE):
            if i == 0 or j == 0 or i == BATTLEFIELD_SIZE -1 or j == BATTLEFIELD_SIZE - 1:
                tmp.append(STAR)
            else:
                tmp.append(EMPTY)
        BATTLEFIELD.append(tmp)

def printBattleField():
    print(f"Your statistic is -> Level is {LEVEL}, Total amount of enemies -> {TOTAL_ENEMIES}, Amount of enemies you need to defeat -> {NEEDS_TO_KILL_TOTAL_ENEMIES} , You can go {STEPS} step(s). Wish you luck!\n")
    for i in BATTLEFIELD:
        print(i)

def getPlayerPosition():
    global CURRENT_PLAYER_POS_H, CURRENT_PLAYER_POS_V
    while True:
        pos_h = random.randint(1,BATTLEFIELD_SIZE-1)
        pos_v = random.randint(1,BATTLEFIELD_SIZE-1)
        if BATTLEFIELD[pos_h][pos_v] == EMPTY:
            BATTLEFIELD[pos_h][pos_v] = PLAYER
            CURRENT_PLAYER_POS_H = pos_h
            CURRENT_PLAYER_POS_V = pos_v
            break
        else:
            continue
        return CURRENT_PLAYER_POS_H, CURRENT_PLAYER_POS_V

def getEnemiesPosition(total_enemies):
    for i in range(total_enemies):
        while True:
            pos_h = random.randint(1, BATTLEFIELD_SIZE-1)
            pos_v = random.randint(1, BATTLEFIELD_SIZE-1)

            if BATTLEFIELD[pos_h][pos_v] == EMPTY:
                BATTLEFIELD[pos_h][pos_v] = ENEMY
                break

def goTo():
    global CURRENT_PLAYER_POS_H, CURRENT_PLAYER_POS_V
    global DEFEATED_ENEMIES, PLAYER, NEEDS_TO_KILL_TOTAL_ENEMIES, STEPS

    while STEPS > 0:
        you_go_to = input(
            f"To go up -> press {DIRECTIONS[0]}, to go down -> press {DIRECTIONS[1]}, to go to the right -> press {DIRECTIONS[2]}, to go to the left -> press {DIRECTIONS[3]}\n-> ")

        if you_go_to not in DIRECTIONS:
            print("Invalid input! Try again")
            continue

        new_h, new_v = CURRENT_PLAYER_POS_H, CURRENT_PLAYER_POS_V

        if you_go_to == DIRECTIONS[0]:
            new_h -= 1
        elif you_go_to == DIRECTIONS[1]:
            new_h += 1
        elif you_go_to == DIRECTIONS[2]:
            new_v += 1
        elif you_go_to == DIRECTIONS[3]:
            new_v -= 1

        if new_h < 0 or new_h >= BATTLEFIELD_SIZE or new_v < 0 or new_v >= BATTLEFIELD_SIZE:
            print("Invalid input or obstacle in the way! Try again")
            continue

        if BATTLEFIELD[new_h][new_v] == ENEMY:
            BATTLEFIELD[new_h][new_v] = EMPTY
            BATTLEFIELD[CURRENT_PLAYER_POS_H][CURRENT_PLAYER_POS_V] = EMPTY
            CURRENT_PLAYER_POS_H, CURRENT_PLAYER_POS_V = new_h, new_v
            BATTLEFIELD[CURRENT_PLAYER_POS_H][CURRENT_PLAYER_POS_V] = PLAYER
            DEFEATED_ENEMIES += 1
            STEPS += 5
            NEEDS_TO_KILL_TOTAL_ENEMIES -= 1
            print(
                f"CONGRATULATIONS! You defeated the enemy! You need to defeat {NEEDS_TO_KILL_TOTAL_ENEMIES} more to go to the next level!")
        elif BATTLEFIELD[new_h][new_v] == EMPTY:
            BATTLEFIELD[CURRENT_PLAYER_POS_H][CURRENT_PLAYER_POS_V] = EMPTY
            BATTLEFIELD[new_h][new_v] = PLAYER
            CURRENT_PLAYER_POS_H, CURRENT_PLAYER_POS_V = new_h, new_v
            STEPS = STEPS - 1


        printBattleField()

        if NEEDS_TO_KILL_TOTAL_ENEMIES == 0:
            break

        if STEPS == 0:
            print("You lost! Game over!")
            return

def nextLevel():
    global LEVEL, TOTAL_ENEMIES, DEFEATED_ENEMIES, NEEDS_TO_KILL_TOTAL_ENEMIES
    if DEFEATED_ENEMIES == TOTAL_ENEMIES:
        TOTAL_ENEMIES = TOTAL_ENEMIES + 1
        LEVEL = LEVEL + 1
        DEFEATED_ENEMIES = 0
        NEEDS_TO_KILL_TOTAL_ENEMIES = TOTAL_ENEMIES
        getEnemiesPosition(TOTAL_ENEMIES)
        print("Hoooray! You won! Welcome to the next level!")
        printBattleField()



def startGame():
    global LEVEL, TOTAL_ENEMIES, DEFEATED_ENEMIES,NEEDS_TO_KILL_TOTAL_ENEMIES, STEPS

    print(f'Welcome to the game! You are {PLAYER}, your enemies look like {ENEMY}, your aim is -> Defeat all the enemies with minimum steps!')
    createBattleField()
    getPlayerPosition()
    getEnemiesPosition(TOTAL_ENEMIES)
    printBattleField()

    while LEVEL >= 0 and NEEDS_TO_KILL_TOTAL_ENEMIES > 0 and STEPS > 0:
        goTo()
        if NEEDS_TO_KILL_TOTAL_ENEMIES == 0:
            nextLevel()

