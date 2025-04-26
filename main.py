import random
import os

char = None

stage = 1
enemyeasy = None
enemyboss = None

# Characters to select
class player:
    def __init__(self, hp, maxhp, mp, maxmp, heal, crit, damage, cost, healcost, sleep):
        self.hp = hp
        self.maxhp = maxhp
        self.mp = mp
        self.maxmp = maxmp
        self.heal = heal
        self.crit = crit
        self.damage = damage
        self.cost = cost
        self.healcost = healcost
        self.sleep = sleep
    
    def attackmove(self):
        if self.mp >= self.cost:
            self.mp - self.cost = self.mp
            crithit = random.randomint(1,20)
            if crithit > self.crit:
                global attack
                attack = self.damage * 2
                print(f"Critical hit! You've done {attack} damage!")
            else:
                attack = self.damage
                print(f"You've done {attack} damage!")
        else:
            print("Not enough MP to do attack!")

    def healmove(self):
        if self.mp >= self.healcost:
            self.hp + self.heal = self.hp
            print(f"You heal yourself for {self.hp} HP!")
            if self.hp > self.maxhp:
                self.hp = self.maxhp
        else:
            print("Not enough MP to heal!")
    
    def sleepmove(self):
        self.mp + self.sleep = self.mp
        if self.mp > self.maxmp:
            self.mp = self.maxmp

class enemy:
    def __init__(self, hp, maxhp, mp, maxmp, miss, damage, cost):
        self.hp = hp
        self.maxhp = maxhp
        self.mp = mp
        self.maxmp = maxmp
        self.miss = miss
        self.damage = damage
        self.cost = cost

        def enemyattack(self):
            if self.mp >= self.cost:
                self.mp - self.cost = self.mp
                missed = random.randomint(1,20)
                if missed < self.miss:
                    global attack
                    attack = self.damage * 2
                    print(f"Critical hit! You've done {attack} damage!")
                else:
                    attack = self.damage
                    print(f"You've done {attack} damage!")
            else:
                print("ERROR!")

        def enemysleep(self):
            self.mp + self.sleep = self.mp
            if self.mp > self.maxmp:
                self.mp = self.maxmp


def clear():
    os.system('cls')

def charselect():
    clear()
    global char
    print("Select a character:")
    print("[1] - Basic Character - 10HP 10MP")
    print("[0] - Back to Menu")

    select = int(input("> "))
    if select == 1:
        char = player(10,10,10,10,2,3,3) # Base Character
    elif select == 0:   
        clear()
        gamemenu()

def stats():
    print("- Character Status - ")
    print("HP:", char.hp, "/", char.maxhp)
    print("MP:", char.mp, "/", char.maxmp)

def gamemenu():
    clear()
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
    elif menu == 3:
        print("Bye!")
    else:
        print("Unknown command! Type a number!")
        gamemenu()

def about():
    clear()
    print("This game was made while having programming classes")
    print("Python was a language i got quickly used to! :D")
    print("I hope you enjoy a bit of this game, the same way")
    print("i've enjoyed making it! :3\n")
    input("> ")
    clear()
    gamemenu()

def battle():
    if stage == 1:
        enemybattle()
    elif stage == 3:
        bossbattle()

def enemybattle():
    enemyeasy = enemy(5,5,5,10,4)

def bossbattle():
    enemyboss = enemy(8,8,8,3,6)
    

# Main function to move the game
def start():
    charselect()

clear()
gamemenu()

# Just so the game doesn't disappear after ending
end = input("> ")