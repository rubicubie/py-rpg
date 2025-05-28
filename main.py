import random
import os
from sys import exit

char = None
stage = 1
enemyeasy = None
enemyboss = None

# Character and Enemy
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
        self.mp -= self.cost
        crithit = random.randomint(1,20)
        if crithit > self.crit:
            global attack
            attack = self.damage * 2
            print(f"Critical hit! You've done {attack} damage!")
        else:
            attack = self.damage
            print(f"You've done {attack} damage!")

    def healmove(self):
        self.hp += self.heal
        print(f"You heal yourself for {self.hp} HP!")
        if self.hp > self.maxhp:
            self.hp = self.maxhp
    
    def sleepmove(self):
        self.mp += self.sleep
        if self.mp > self.maxmp:
            self.mp = self.maxmp
    
    def stats(self):
        print("- Character Status - ")
        print("HP:", self.hp, "/", self.maxhp)
        print("MP:", self.mp, "/", self.maxmp)


class enemy:
    def __init__(self, hp, maxhp, mp, maxmp, miss, damage, cost):
        self.hp = hp
        self.maxhp = maxhp
        self.mp = mp
        self.maxmp = maxmp
        self.miss = miss
        self.damage = damage
        self.cost = cost

    def enemyattackmove(self):
        if self.mp >= self.cost:
            self.mp -= self.cost
            missed = random.randomint(1,20)
            if missed < self.miss:
                global enemyattack
                enemyattack = 0
                print(f"The enemy missed their attack!")
            else:
                enemyattack = self.damage
                print(f"The enemy did {enemyattack} damage!")
        else:
            print("ERROR! ")

    def enemysleepmove(self):
        self.mp += self.sleep
        if self.mp > self.maxmp:
            self.mp = self.maxmp
        
    def enemyai(self):
        if self.hp > 0:
            if self.cost > self.mp:
                enemy.enemysleepmove()
            elif self.cost <= self.mp:
                enemy.enemyattackmove()
            else:
                print("ERROR! Enemy couldn't decide between sleeping or attacking! Report this!")
        else:
            global stage
            stage += 1
            print("You won! Next stage!")
            input("> ")
    
    def stats(self):
        if stage // 3 == 0:
            print("-*- Boss Status -*-")
            print("HP:", self.hp, "/", self.maxhp)
            print("MP:", self.mp, "/", self.maxmp)
        else:
            print("- Enemy Status - ")
            print("HP:", self.hp, "/", self.maxhp)
            print("MP:", self.mp, "/", self.maxmp)
# -- -- --

def clear():
    os.system('cls')

def gamemenu():
    clear()
    print("- Python RPG -\n")
    print("[1] - START")
    print("[2] - ABOUT")
    print("[3] - EXIT")
    try:
        menu = int(input("> "))
    except:
        gamemenu()
    if menu == 1 :
        clear()
        start()
    elif menu == 2:
        clear()
        about()
    elif menu == 3:
        clear()
        print("Bye!")
    else:
        print("Unknown command! Type a number!")
        gamemenu()

def charselect():
    clear()
    global char
    print("Select a character:")
    print("[1] - Basic Character - 10HP 10MP")
    print("[0] - Back to Menu")

    select = input("> ")
    select = int(select)
    #try:
    if select == 1:
        # Character: player(hp,maxhp,mp,maxmp,heal,crit,damage,cost,healcost,sleep)
        char = player(10, 10, 10, 10, 2, 3, 3, 4, 5, 8) # Base Character
    elif select == 0:   
        clear()
        gamemenu()
    else:
        print("Unknown command! Type a number!")
        input("> ")
        charselect()

    # Difficulty selection ( add settings for this later )
    # Enemy: enemy(hp, maxhp, mp, maxmp, miss, damage, cost)
    global enemyeasy
    global enemyboss
    enemyeasy = enemy(5, 5, 8, 8, 6, 4, 3)
    enemyboss = enemy(8, 8, 8, 8, 3, 5, 3)
    battle()
    #except:
        #clear()
        #print("ERROR! Something went wrong while selecting your character!")
        #print("Press [ENTER] to go back to character selecting")
        #input("> ")
        #charselect()

def about():
    clear()
    print("This game was made while having programming classes")
    print("Python was a language i got quickly used to! :D")
    print("I hope you enjoy a bit of this game, the same way")
    print("i've enjoyed making it! :3\n")
    input("> ")
    gamemenu()

def battle():
    global enemytype
    if stage // 3 == 0:
        enemytype = enemyboss
    else:
        enemytype = enemyeasy
    playerturn()
        

def playerturn():
    clear()
    print("Your turn!")
    char.stats()
    enemytype.stats()
    print("Select a move:")
    print(f"[1] Attack [-{char.cost} MP]")
    print(f"[2] Sleep [+{char.sleep} MP]")
    if char.heal >= 1:
        global healer
        healer = 1
        print(f"[3] Heal [+{char.heal} -{char.healcost}]")
    healer = 0
    playeroptions()

def playeroptions():
    turn = input("> ")
    if turn == 1:
        if char.mp >= char.cost:
            char.attackmove()
        else:
            print("You don't have enough MP for this move!")
    elif turn == 2:
        if char.mp != char.maxmp:
            char.sleepmove()
    elif turn == 3 and healer == 1:
        if char.mp >= char.healcost:
            char.healmove()
        else:
            print("You don't have enough MP for this move!")
    else:
        clear()
        playerturn()

# Main function to move the game
def start():
    charselect()

clear()
gamemenu()

# Just so the game doesn't disappear after ending
end = input("> ")