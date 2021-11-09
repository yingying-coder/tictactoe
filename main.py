from coordinate import locations
from gamer import Gamer
from board import Board
from random import choice


def is_draw():
    draw = False
    if len(locations) == 0:
        print("Game Over\nDraw!")
        draw = True
    return draw


def game(board, gamer, location):
    pos = gamer.move(location)
    board.update(pos, gamer.sign)


board = Board()
prompt = input("Enter X or O to choose your player: ")
if prompt == "X":
    player = Gamer("You", "X")
    ai = Gamer("Computer", "O")
    board.print_board()
else:
    player = Gamer("You", "O")
    ai = Gamer("Computer", "X")
    locc = choice(locations)
    game(board, ai, locc)
    board.print_board()
game_over = False
while not game_over:
    locp = input("enter the number you want to locate: ")
    game(board, player, locp)
    if player.is_win() or is_draw():
        board.print_board()
        game_over = True
        break
    else:
        if ai.check():
            locc = choice(ai.check())
        elif player.check():
            locc = choice(player.check())
        else:
            locc = choice(locations)
        game(board, ai, locc)
        board.print_board()
        if ai.is_win() or is_draw():
            game_over = True

