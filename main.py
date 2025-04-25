import random

print("- RPG game test -")
input("[ENTER] Start")

# Characters to select

bas = {
    "hp" = 10,
    "maxhp" = 10,
    "mp" = 10,
    "maxmp" = 10
}

def charselect():
    print("Select a character:")
    print("bas - Base Character - 10HP 10MP")

def stats():
    print("- Character Status - ")
    print("HP:", hp, "/", maxhp)
    print("MP:", mp, "/", maxmp)
    