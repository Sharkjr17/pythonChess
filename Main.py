import time
import random
import array
import sys, subprocess
import math
import BoardPrinter
import Extras

#Create vital variables

currentTurn = 1
currentPlayer = "Lowercase"






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
    


def turn():
    print()
    if currentTurn % 2 == 0:
      currentPlayer = "Uppercase"
    if currentTurn % 2 == 1:
      currentPlayer = "Lowercase"
    #Print out what turn it is
    print("Turn: " + str(currentTurn))
    print("Player: " + currentPlayer)
    print()

    #Print out the current board
    print("Current Board:")
    BoardPrinter.printBoard()
    print()

    #Begin player input
    print("Choose a piece position:")
    print()
    i = input().upper
    chosenPosition = 0

    #Extremely stupid way to find chosen position

    #Column:
    if(i(1) == "1"):
      chosenPosition = -1
    elif(i(1) == "2"):
      chosenPosition = 7
    elif(i(1) == "3"):
      chosenPosition = 15
    elif(i(1) == "4"):
      chosenPosition == 23
    elif(i(1) == "5"):
      chosenPosition == 31
    elif(i(1) == "6"):
      chosenPosition == 39
    elif(i(1) == "7"):
      chosenPosition == 47
    elif(i(1) == "8"):
      chosenPosition == 55
    else:
      #If the player sucks at putting in numbers
      print("Invalid input! Try again loser!")
      turn()

    #Convert row to integer
    if(i(0) == "A"):
      rowVal = 1
    elif(i(0) == "B"):
      rowVal = 1
    elif(i(0) == "C"):
      rowVal = 1
    elif(i(0) == "D"):
      rowVal = 1
    elif(i(0) == "E"):
      rowVal = 1
    elif(i(0) == "F"):
      rowVal = 1
    elif(i(0) == "G"):
      rowVal = 1
    elif(i(0) == "H"):
      rowVal = 1
      
    if(i(0) == "1"):
      chosenPosition = -1
    elif(i(0) == "2"):
      chosenPosition = 7
    elif(i(0) == "C"):
      chosenPosition = 15
    elif(i(0) == "D"):
      chosenPosition == 23
    elif(i(0) == "E"):
      chosenPosition == 31
    elif(i(0) == "F"):
      chosenPosition == 39
    elif(i(0) == "G"):
      chosenPosition == 47
    elif(i(0) == "H"):
      chosenPosition == 55
    else:
      #If the player sucks at putting in letters
      print("Invalid input! Try again loser!")
      turn()

    #Put the row into it baby
    chosenPosition = chosenPosition + i(1)

    


def positionScan(int):
  boardPos = BoardPrinter.board[int]



#Run The Game
def gameStart():
    guide()

    turn()

#Run The Script (To Run The Game!)
subprocess.run('clear', shell=True)
gameStart()
