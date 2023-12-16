# Игра ПК угадывает ваше задуманное число

import random

print("What is your name? : ")
name = input()
print(name, ", please, select any number from 1 to 10", sep="")
NUM = int(input())

if (NUM >= 1) and (NUM <= 10):
    i = 0
    randNum = 0
    while i < 100:
        i += 1
        randNum = random.randint(1, 10)
        print(i, ") Is your number: ", randNum, " ? ", end="", sep="")
        if randNum == NUM:
            print("Yes!")
            break
        else:
            print("No")
    if randNum != NUM:
        print("Can not guess your num! =(")
