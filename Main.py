import time
import random
import array

# ♔	 ♕	♖	♗	♘	♙	♚	♛	♜	♝	♞	♟
#create le funny printing function
def scanPrint(str):


Board = ["X", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-"]

def printBoard():

    #Row A
    print(Board[1:9])
    #Row B
    print(Board[9:17])
    #Row C
    print(Board[17:25])
    #Row D
    print(Board[25:33])
    #Row E
    print(Board[33:41])
    #Row F
    print(Board[41:49])
    #Row G
    print(Board[49:57])
    #Row H
    print(Board[57:65])

printBoard()


