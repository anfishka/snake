import random

BATTLE_FIELD_SIZE = 10
BATTLE_FIELD = []
STAR = "*"
EMPTY = " "
ENEMY = "+"
PLAYER = "@"
LEVEL = 1
PLAYER_MOVES = 5
TOTAL_ENEMIES = 3
DIRECTIONS = ["W", "A", "D", "S"]

for i in range(BATTLE_FIELD_SIZE):
    tmp_field = []
    for j in range(BATTLE_FIELD_SIZE):
        if i == 0 or j == 0 or (i == BATTLE_FIELD_SIZE - 1 and j < BATTLE_FIELD_SIZE) or (
                j == BATTLE_FIELD_SIZE - 1 and i < BATTLE_FIELD_SIZE):
            tmp_field.append(STAR)
        else:
            tmp_field.append(EMPTY)
    BATTLE_FIELD.append(tmp_field)

player_pos_h = random.randrange(1, BATTLE_FIELD_SIZE - 1)
player_pos_v = random.randrange(1, BATTLE_FIELD_SIZE - 1)
BATTLE_FIELD[player_pos_h][player_pos_v] = PLAYER


def random_pos():
    rand_pos_h = random.randrange(1, BATTLE_FIELD_SIZE - 1)
    rand_pos_v = random.randrange(1, BATTLE_FIELD_SIZE - 1)
    return rand_pos_h, rand_pos_v


def create_enemies():
    for i in range(TOTAL_ENEMIES):
        enemy_pos_h, enemy_pos_v = random_pos()
        while BATTLE_FIELD[enemy_pos_h][enemy_pos_v] != EMPTY:
            enemy_pos_h, enemy_pos_v = random_pos()
        BATTLE_FIELD[enemy_pos_h][enemy_pos_v] = ENEMY

create_enemies()

DEFEATED_ENEMIES = 0

while True:
    if PLAYER_MOVES == 0:
        print("Game over! You ran out of moves.")
        break

    print("Level: ",LEVEL)
    print("Player moves left: ", PLAYER_MOVES)
    print("Defeated enemies: ", DEFEATED_ENEMIES , "/", TOTAL_ENEMIES)

    for i in BATTLE_FIELD:
        print(i)

    direction = input("Choose direction -> D - go to the right, A - go to the left, W - go up, S - go down -> ")
    if direction not in DIRECTIONS:
        print("Invalid direction! Try again!")
        continue

    for i in range(BATTLE_FIELD_SIZE):
        for j in range(BATTLE_FIELD_SIZE):
            if BATTLE_FIELD[i][j] == PLAYER:
                player_pos_h, player_pos_v = i, j
                break

    new_player_pos_h, new_player_pos_v = player_pos_h, player_pos_v

    if direction == DIRECTIONS[0]:
        new_player_pos_h -= 1
    elif direction == DIRECTIONS[1]:
        new_player_pos_v -= 1
    elif direction == DIRECTIONS[2]:
        new_player_pos_v += 1
    elif direction == DIRECTIONS[3]:
        new_player_pos_h += 1

    if not (1 <= new_player_pos_h < BATTLE_FIELD_SIZE - 1) or not (1 <= new_player_pos_v < BATTLE_FIELD_SIZE - 1):
        print("Invalid move! You can't go outside the battlefield!")
        continue

    if BATTLE_FIELD[new_player_pos_h][new_player_pos_v] == EMPTY:
        BATTLE_FIELD[player_pos_h][player_pos_v] = EMPTY
        BATTLE_FIELD[new_player_pos_h][new_player_pos_v] = PLAYER
        player_pos_h, player_pos_v = new_player_pos_h, new_player_pos_v
        PLAYER_MOVES -= 1

    elif BATTLE_FIELD[new_player_pos_h][new_player_pos_v] == ENEMY:
        BATTLE_FIELD[new_player_pos_h][new_player_pos_v] = EMPTY
        DEFEATED_ENEMIES += 1
        PLAYER_MOVES += 5
        print("You defeated an enemy!")

    if DEFEATED_ENEMIES >= TOTAL_ENEMIES:
        print("Congratulations! You defeated all the enemies.")
        LEVEL += 1
        TOTAL_ENEMIES += 1
        DEFEATED_ENEMIES = 0
        PLAYER_MOVES = 5
        create_enemies()

