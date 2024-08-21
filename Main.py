import time
import random
import array

#Create vital variables
Board = [
         "R", "N", "B", "Q", "K", "B", "N", "R", 
         "P", "P", "P", "P", "P", "P", "P", "P", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "p", "p", "p", "p", "p", "p", "p", "p", 
         "r", "n", "b", "q", "k", "b", "n", "r"]
currentTurn = 1
currentPlayer = "Lower case"

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

def turn():
    print()
    
def gameStart():
    scanPrint("Welcome to ultimate chess!")
    scanPrint("==========================")
    scanPrint("Would you like a quick guide?")
    print()
    guide = input("Yes or no: ")

    guide = guide.upper()

    if((guide == "YES") or (guide == "Y")):
       pass

    turn()

gameStart()
