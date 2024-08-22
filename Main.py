import time
import random
import array
import sys, subprocess
import math

#Create vital variables
Board = [
         "1", "N", "B", "Q", "K", "B", "N", "8", 
         "P", "P", "P", "P", "P", "P", "P", "P", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-",
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "p", "p", "p", "p", "p", "p", "p", "p", 
         "9", "n", "b", "q", "k", "b", "n", "1"]
currentTurn = 1
currentPlayer = "Lowercase"

#Defines function that prints text awesome style for cooler text
def scanPrint(str):
  step = 0
  inputText = str
  length = len(inputText)
  
  while(step < length):
    print(inputText[0: step + 1], end = "\r")

    time.sleep(0.02)

    step = step + 1

  print("\r");

#Prints the board for the player to see
def printBoard():

    if currentPlayer == "Lowercase":
        #Column labels
        print("     a   b   c   d   e   f   g   h")
        #Top buffer
        print(" ==================================")

        #Row prints include row labels from 8 to 1, top-down

        #Row 8
        print("8|  ",Board[0]," ",Board[1]," ",Board[2]," ",Board[3]," ",Board[4]," ",Board[5]," ",Board[6]," ",Board[7])
        #Row 7
        print("7|  ",Board[8]," ",Board[9]," ",Board[10]," ",Board[11]," ",Board[12]," ",Board[13]," ",Board[14]," ",Board[15])
        #Row 6
        print("6|  ",Board[16]," ",Board[17]," ",Board[18]," ",Board[19]," ",Board[20]," ",Board[21]," ",Board[22]," ",Board[23])
        #Row 5
        print("5|  ",Board[24]," ",Board[25]," ",Board[26]," ",Board[27]," ",Board[28]," ",Board[29]," ",Board[30]," ",Board[31])
        #Row 4
        print("4|  ",Board[32]," ",Board[33]," ",Board[34]," ",Board[35]," ",Board[36]," ",Board[37]," ",Board[38]," ",Board[39])
        #Row 3
        print("3|  ",Board[40]," ",Board[41]," ",Board[42]," ",Board[43]," ",Board[44]," ",Board[45]," ",Board[46]," ",Board[47])
        #Row 2
        print("2|  ",Board[48]," ",Board[49]," ",Board[50]," ",Board[51]," ",Board[52]," ",Board[53]," ",Board[54]," ",Board[55])
        #Row 1
        print("1|  ",Board[56]," ",Board[57]," ",Board[58]," ",Board[59]," ",Board[60]," ",Board[61]," ",Board[62]," ",Board[63])
    elif currentPlayer == "Uppercase":
        #Column labels
        print("     h   g   f   e   d   c   b   a")
        #Top buffer
        print(" ==================================")

        #Row prints include row labels from 1 to 8, top-down

        #Row 1
        print("8|  ",Board[63]," ",Board[62]," ",Board[61]," ",Board[60]," ",Board[59]," ",Board[58]," ",Board[57]," ",Board[56])
        #Row 2
        print("7|  ",Board[55]," ",Board[54]," ",Board[53]," ",Board[52]," ",Board[51]," ",Board[50]," ",Board[49]," ",Board[48])
        #Row 3
        print("6|  ",Board[47]," ",Board[46]," ",Board[45]," ",Board[44]," ",Board[43]," ",Board[42]," ",Board[41]," ",Board[40])
        #Row 4
        print("5|  ",Board[39]," ",Board[38]," ",Board[37]," ",Board[36]," ",Board[35]," ",Board[34]," ",Board[33]," ",Board[32])
        #Row 55
        print("4|  ",Board[31]," ",Board[30]," ",Board[29]," ",Board[28]," ",Board[27]," ",Board[26]," ",Board[25]," ",Board[24])
        #Row 6
        print("3|  ",Board[23]," ",Board[22]," ",Board[21]," ",Board[20]," ",Board[19]," ",Board[18]," ",Board[17]," ",Board[16])
        #Row 7
        print("2|  ",Board[15]," ",Board[14]," ",Board[13]," ",Board[12]," ",Board[11]," ",Board[10]," ",Board[9]," ",Board[8])
        #Row 8
        print("1|  ",Board[7]," ",Board[6]," ",Board[5]," ",Board[4]," ",Board[3]," ",Board[2]," ",Board[1]," ",Board[0])





def guide():
    scanPrint("Welcome to ultimate chess!")
    scanPrint("==========================")
    scanPrint("Would you like a quick guide?")
    print()
    guide = input("Yes or no: ").upper()
    subprocess.run('clear', shell=True)
    if((guide == "YES") or (guide == "Y")):
        print()
        print("Python chess is probably the worst version of chess")
        print()
        print("To read the board, understand the following symbols:")
        print("====================================================")
        scanPrint("P/p = Pawn")
        scanPrint("R/r = Rook")
        scanPrint("N/n = Knight")
        scanPrint("B/b = Bishop")
        scanPrint("K/k = King")
        scanPrint("Q/q = Queen")
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
    scanPrint("Current Board:")
    printBoard()
    print()

    #Begin player input
    scanPrint("Choose a piece position:")
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
    else:
      #If the player sucks at putting in letters
      print("Invalid input! Try again loser!")
      turn()

    #Put the row into it baby
    chosenPosition = chosenPosition + i(1)








#Run The Game
def gameStart():
    guide()

    turn()

#Run The Script
subprocess.run('clear', shell=True)
gameStart()
