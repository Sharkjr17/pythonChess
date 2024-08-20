#My Peanits

import time
import random
import array

#create le funny printing function
def scanPrint(str):

    step = 0
    inputText = str
    length = len(inputText)

    while(step < length):

        print(inputText[0: step + 1], end = "\r")
        time.sleep(0.02)
        step = step + 1

    print("\r")
