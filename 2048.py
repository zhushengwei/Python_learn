# coding:utf-8
import curses
from random import randrange, choice
from collections import defaultdict

# 用户行为
actions = ['Up', 'Left', 'Down', 'Right', 'Restart', 'Exit']
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions_dict = dict(zip(letter_codes, actions * 2))

def main(stdscr):
    def init():
        return 'Game'

    def not_game(state):
        responses = defaultdict(lambda : state)
        responses['Restart'], responses['Exit'] = 'Init', 'Exit'
        return responses[actions]

    def game():
        if actions == 'Restart':
            return 'Init'

        if actions == 'Exit':
            return 'Exit'


def get_user_action(keyboard):
    char = 'N'
    while char not in actions_dict:
        char = keyboard.getch()
        return actions_dict[char]

def transpose(field):
    return [list(row) for row in zip(*field)]

def invert(field):
    return [row[::1] for row in field]

class GameField(object):
    def __init__(self, height=4, width=4):
        self.height = height
        self.width = width
        self.win_value = 2048
        self.score = 0
        self.highscore = 0
        self.reset()



