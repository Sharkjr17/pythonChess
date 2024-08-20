import time
import random
import array
from colorama import Fore




Board = [
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "P", "P", "P", "P", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-", 
         "-", "-", "-", "-", "-", "-", "-", "-"]

def printBoard():

    #Row A
    print(Board[0:8])
    #Row B
    print(Board[8:16])
    #Row C
    print(Board[16:24])
    #Row D
    print(Board[24:32])
    #Row E
    print(Board[32:40])
    #Row F
    print(Board[40:48])
    #Row G
    print(Board[48:56])
    #Row H
    print(Board[56:64])

    for i in range(len(Board)):
            print(f"{Fore.RED}" + Board[i], end = " ")
printBoard()

print(f"{Fore.RED}This text is red!{Fore.WHITE}")
print(14%7)
