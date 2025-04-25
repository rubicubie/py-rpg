import random
import os

def clear():
    os.system('cls')

# Characters to select
char = 0

# Basic Character
base = {
    "hp": 10,
    "maxhp": 10,
    "mp": 10,
    "maxmp": 10,
    "crit": 1 # Gonna make crits later
}

def charselect():
    print("Select a character:")
    print("[1] - Basic Character - 10HP 10MP")

    char = input("> ")
    if char == 1:
        char = "base"

def stats():
    print("- Character Status - ")
    print("HP:", char.get("hp"), "/", char.get("maxhp"))
    print("MP:", char.get("mp"), "/", char.get("maxmp"))


# Game Start
print("- The RPG with barely no RNG, trust me -\n")
print("[1] - START")
print("[2] - ABOUT")
print("[3] - EXIT")