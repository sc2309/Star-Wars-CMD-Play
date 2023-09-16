import sys
from music import *

def P1Strike(h,sh,shand,sb,sl,c,h2,sh2,shand2,sb2,sl2,c2):
    print("Select your move P1 \nlightsaber strike on head(lsh)\nlightsaber strike on hand(lshand)\nlightsaber strike on leg(lsl)\nlightsaber strike on body(lsb)\nchoke opponents neck(c)\n")
    move = input()
    if move == 'lsh':
        h2 = h2 - sh
    elif move == 'lshand':
        h2 = h2 - shand
    elif move == 'lsl':
        h2 = h2 - sl
    elif move == 'lsb':
        h2 = h2 - sb
        if h + 50 != 500 and h < 450:
            h = h + 50
        elif h + 50 == 500 or h > 450 and h < 500:
            h = 500
        else:
            pass
    elif move == 'c':
        h2 = h2 - c
    else:
        print('missed')
    print("P2's health is,",h2,"\n")
    if h2 == 0 or h2 < 0:
        print("P2 lost the game\nThanks for playing! may the force be with you.")
        play_music()
        sys.exit()
    P2Strike(h,sh,shand,sb,sl,c,h2,sh2,shand2,sb2,sl2,c2)

def P2Strike(h,sh,shand,sb,sl,c,h2,sh2,shand2,sb2,sl2,c2):
    print("Select your move P2\nlightsaber strike on head(lsh)\nlightsaber strike on hand(lshand)\nlightsaber strike on leg(lsl)\nlightsaber strike on body(lsb)\nchoke opponents neck(c)\n\n")
    move = input()
    if move == 'lsh':
        h = h - sh2
    elif move == 'lshand':
        h = h - shand2
    elif move == 'lsl':
        h = h - sl2
    elif move == 'lsb':
        h = h - sb2
        if h2 + 50 != 500:
            h2 = h2 + 50
        elif h2 + 50 == 500 or h2 > 450:
            h2 = 500
        else:
            pass
    elif move == 'c':
        h = h - c2
    else:
        print('missed')
    print("P1's health is,",h,"\n")
    if h == 0 or h < 0:
        print("P1 lost the game\nThanks for playing! may the force be with you.")
        play_music()
        sys.exit()
    P1Strike(h,sh,shand,sb,sl,c,h2,sh2,shand2,sb2,sl2,c2)