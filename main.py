import random
import PySimpleGUI as pg


moveCount = random.randint(20,30)

possibleMoves = ["F", "F'", "B", "B'", "U", "U'", "D", "D'","R", "R'", "L", "L'"]
scrambled = []



while moveCount > 0:
    moveCount -= 1
    move = random.choice(possibleMoves)
    scrambled.append(move)

print(scrambled)


