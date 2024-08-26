import time
import random
import array
import sys, subprocess
import math
import BoardPrinter
import Extras



def guide():
    Extras.scanPrint("Welcome to ultimate chess!")
    Extras.scanPrint("==========================")
    Extras.scanPrint("Would you like a quick guide?")
    print()
    guide = input("Yes or no: ").upper()
    subprocess.run('clear', shell=True)
    if((guide == "YES") or (guide == "Y")):
        print()
        print("Python chess is probably the worst version of chess")
        print()
        print("To read the board, understand the following symbols:")
        print("====================================================")
        Extras.scanPrint("P/p = Pawn")
        Extras.scanPrint("R/r = Rook")
        Extras.scanPrint("N/n = Knight")
        Extras.scanPrint("B/b = Bishop")
        Extras.scanPrint("K/k = King")
        Extras.scanPrint("Q/q = Queen")
    i = input("Press Enter to Continue")
    subprocess.run('clear', shell=True)
    


#Run The Game
def gameStart():
    guide()

    BoardPrinter.turn()

#Run The Script (To Run The Game!)
subprocess.run('clear', shell=True)
gameStart()
