import random
import os

char = None

def clear():
    os.system('cls')

# Characters to select
class player:
    def __init__(self, hp, maxhp, mp, maxmp, crit):
        self.hp = hp
        self.maxhp = maxhp
        self.mp = mp
        self.maxmp = maxmp
        self.crit = crit

def charselect():
    clear()
    print("Select a character:")
    print("[1] - Basic Character - 10HP 10MP")
    print("[0] - Back to Menu")

    select = int(input("> "))
    if select == 1:
        char = player(10,10,10,10,2)
        print("CHARACTER CHANGED")
    elif select == 0:   
        clear()
        gamemenu()

def stats():
    clear()
    print(char)
    print("- Character Status - ")
    print("HP:", char.hp, "/", char.maxhp)
    print("MP:", char.mp, "/", char.maxmp)

def gamemenu():
    print("- Python RPG -\n")
    print("[1] - START")
    print("[2] - ABOUT")
    print("[3] - EXIT")
    menu = int(input("> "))
    print(menu)

    if menu == 1 :
        clear()
        start()
    elif menu == 2:
        clear()
        about()
    else:
        clear()
        print("Bye!")

def about():
    clear()
    print("This game was made while having programming classes")
    print("Python was a language i got quickly used to! :D")
    print("I hope you enjoy a bit of this game, the same way")
    print("i've enjoyed making it! :3\n")
    input("> ")
    gamemenu()

# Main function to move the game
def start():
    charselect()

gamemenu()
end = input("> ")
stats()

# Just so the game doesn't disappear after ending
end = input("> ")