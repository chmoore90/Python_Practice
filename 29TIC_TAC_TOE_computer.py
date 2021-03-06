# Tic tac toe, but against the computer.

import random


def reset(game, turns_taken, state):
    game.clear()
    game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    turns_taken.clear()
    state = "play on"
    return game, turns_taken, state


def top(row):
    return f" --- --- ---\n| {row[0]} | {row[1]} | {row[2]} |"


def mid(row):
    return f"\n --- --- ---\n| {row[0]} | {row[1]} | {row[2]} |"


def bot(row):
    return f"\n --- --- ---\n| {row[0]} | {row[1]} | {row[2]} |\n --- --- ---"


def draw(turns_taken, game):
    for turn in turns_taken:
        x, y = turn["coords"]
        game[y - 1][x - 1] = player_marks[turn["player"]]

    print("".join(list((top(game[2]), mid(game[1]), bot(game[0])))))


def welcome():
    print(
        "Welcome to Chloe's Tic Tac Toe!\nThe game board uses (x,y) coordinates as input to place your markers."
    )
    print(
        "Use a comma to separate x and y. You don't need to use any spaces or parentheses."
    )
    print(
        "".join(
            list(
                [
                    "      ----- ----- -----\n   3 |(1,3)|(2,3)|(3,3)|",
                    "\n      ----- ----- -----\nY: 2 |(1,2)|(2,2)|(3,2)|",
                    "\n      ----- ----- -----\n   1 |(1,1)|(2,1)|(3,1)|",
                    "\n      ----- ----- -----",
                    "\nX:      1     2     3",
                ]
            )
        )
    )


def change_player(curr_player):
    if curr_player == player:
        return computer
    else:
        return player


def get_player(turns_taken):
    while True:

        # Get user input
        coords_in = input(f"{player}'s turn. Enter your coordinates: ")

        # Input validation
        try:
            coords_xy = [int(coord) for coord in coords_in.split(",")]

        except ValueError:
            print(
                "Invalid input. X and Y coordinates must be numbers (1, 2, or 3) and separated by a comma."
            )
            continue

        if len(coords_xy) != 2:
            print(
                "Invalid input. Coordinates must be two numbers, separated by a comma."
            )
            continue

        if coords_xy[0] > 3 or coords_xy[1] > 3 or coords_xy[0] < 1 or coords_xy[1] < 1:
            print("Invalid input. X and Y coordinates must be 1, 2, or 3.")
            continue

        # Coordinate validation
        used_coords = {}
        coords = tuple(coords_xy)

        for turn in turns_taken:
            used_coords[turn["coords"]] = turn["player"]

        if coords not in used_coords:
            return coords

        elif curr_player == used_coords[coords]:
            print(f"You already put an {player_marks[player]} here.")
            continue

        else:
            print("The computer is occupying this spot!")
            continue


def get_computer(game, player_marks):

    game_tiles = {
        "top row": [game[2][0], game[2][1], game[2][2]],
        "middle row": [game[1][0], game[1][1], game[1][2]],
        "bottom row": [game[0][0], game[0][1], game[0][2]],
        "first column": [game[2][0], game[1][0], game[0][0]],
        "second column": [game[2][1], game[1][1], game[0][1]],
        "third column": [game[2][2], game[1][2], game[0][2]],
        "top-bottom diagonal": [game[2][0], game[1][1], game[0][2]],
        "bottom-top diagonal": [game[0][0], game[1][1], game[2][2]],
    }

    coords_tiles = {
        "top row": [(1, 3), (2, 3), (3, 3)],
        "middle row": [(1, 2), (2, 2), (3, 2)],
        "bottom row": [(1, 1), (2, 1), (3, 1)],
        "first column": [(1, 3), (1, 2), (1, 1)],
        "second column": [(2, 3), (2, 2), (2, 1)],
        "third column": [(3, 3), (3, 2), (3, 1)],
        "top-bottom diagonal": [(1, 3), (2, 2), (3, 1)],
        "bottom-top diagonal": [(1, 1), (2, 2), (3, 3)],
    }

    # block player
    for key, value in game_tiles.items():
        if value.count(player_marks[player]) == 2:
            try:
                x = value.index(" ")
            except:
                pass
            else:
                coords = coords_tiles.get(key)[x]

                return coords

    # search for win
    for key, value in game_tiles.items():
        if value.count(player_marks[computer]) == 2:
            try:
                y = value.index(" ")
            except:
                pass
            else:
                coords = coords_tiles.get(key)[y]

                return coords

    # place in centre
    if game[1][1] == " ":
        coords = (2, 2)
        return coords

    # place randomly
    while True:

        key_list = list(coords_tiles.keys())
        random_key = key_list[random.randint(0, len(key_list)-1)]
        r = random.randint(0, 2)
        tile = game_tiles.get(random_key)[r]

        if tile != " ":
            continue

        else:
            coords = coords_tiles.get(random_key)[r]
            return coords

    # for key, value in game_tiles.items():
    #     for i in range(len(value)):
    #         if value[i] == " ":
    #             coords = coords_tiles.get(key)[i]

    #             return coords


def add_curr_turn(turns_taken, curr_player, coords):
    curr_turn = {
        "player": curr_player,
        "coords": coords,
    }
    turns_taken.append(curr_turn)


def check_state(game, player_marks, player_counts, turns_taken):

    win_conditions = {
        "top row": game[2][0] == game[2][1] == game[2][2] and game[2][0].split(),
        "middle row": game[1][0] == game[1][1] == game[1][2] and game[1][0].split(),
        "bottom row": game[0][0] == game[0][1] == game[0][2] and game[0][0].split(),
        "first column": game[2][0] == game[1][0] == game[0][0] and game[2][0].split(),
        "second column": game[2][1] == game[1][1] == game[0][1] and game[2][1].split(),
        "third column": game[2][2] == game[1][2] == game[0][2] and game[2][2].split(),
        "top-bottom diagonal": game[2][0] == game[1][1] == game[0][2]
        and game[2][0].split(),
        "bottom-top diagonal": game[0][0] == game[1][1] == game[2][2]
        and game[0][0].split(),
    }

    # Check for a winner
    for key, value in win_conditions.items():
        if value:
            player_counts[curr_player] += 1
            print(
                f"{curr_player} wins! They made a line of {player_marks[curr_player]}'s in the {key}."
            )
            return "game over"

    # Check for a draw
    if len(turns_taken) == 9:
        print("It's a draw!")
        return "game over"

    return "play on"


# GAME CODE STARTS HERE

welcome()

player = input("Enter player name: ")
computer = "Computer"

game = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
turns_taken = []
curr_player = None
state = "play on"

player_marks = {
    player: "X",
    computer: "O",
}
player_counts = {
    player: 0,
    computer: 0,
}


while True:
    while state == "play on":
        curr_player = change_player(curr_player)
        if curr_player == player:
            coords = get_player(turns_taken)
        else:
            coords = get_computer(game, player_marks)
        add_curr_turn(turns_taken, curr_player, coords)
        draw(turns_taken, game)
        state = check_state(game, player_marks, player_counts, turns_taken)

        if state == "game over":
            ready = input("Would you like to play again? ")

            if ready.strip().lower() not in ["y", "yes", "ready", "ok", "1", "true"]:
                print("Thanks for playing! Here are your win tallies:")
                print(f"{player} wins: {player_counts[player]}")
                print(f"{computer} wins: {player_counts[computer]}")
                exit()

            print("Starting a new game. Good luck!")
            game, turns_taken, state = reset(game, turns_taken, state)
            draw(turns_taken, game)
