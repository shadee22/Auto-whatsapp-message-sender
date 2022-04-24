
#PIP INSTALL PYAUTOGUI

import pyautogui as py
import time 

#STARTING INTREVAL FOR BEFORE RUN
#(FOR POSITIONING WHERE WANT TO IT TYPE)
time.sleep(10)

#NAME VARIABLE
name = "Elon Musk"

#FILE FOR ANIMAL NAMES
txt = open('animals.txt' , 'r')

#THIS WILL WRITE ALL ANIMAL NAMES WITH $name variable
for i in txt :
    py.write("Hey " + name + " You are a " + i, interval=0.1)

    py.press("Enter")

#OUTPUT::
Hey Elon Musk You are a Canidae

Hey Elon Musk You are a Felidae

Hey Elon Musk You are a Cat

Hey Elon Musk You are a Cattle

Hey Elon Musk You are a Dog

#...FOREVER YOU ARE GONNA CALL ELON MUSK AS ANIMAL