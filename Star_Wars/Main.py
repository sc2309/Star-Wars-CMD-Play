from start import *
from music import *
import pygame
import sys

def help():
    print('''\nBASIC:\nYour opponent will not be automatic\n\nChoose your character as P1\n
        sometimes a character may undergo aggeression and may\ncause mor damage than normal\n
        more featres will be added in future\n
        ''')

def mainF():
    if __name__ == '__main__':
        play_music()
        print('type p and press enter to play the game\nh for help\ne for exit\n')
        choise = input()
        if choise == 'p':
            Game()
        elif choise == 'h':
            pass
        elif choise == 'e':
            sys.exit()
        else:
            print('Input Error : choise made was invalid\n')

mainF()