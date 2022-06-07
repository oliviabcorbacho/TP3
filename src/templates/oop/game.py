#!/usr/bin/env python3
import time
import mapping
import msvcrt
import random
from human import Human
from items import Item, PickAxe, Sword, Amulet, Food
from gnome import Gnome
import gnome_actions
import actions
from keys import read_single_keypress
from colorama import Fore, Back, Style

import sys
sys.setrecursionlimit(10000)


ROWS = 25
COLUMNS = 80


if __name__ == "__main__":
    # initial parameters
    #level = 0
   # initial locations may be random generated
    print(Fore.YELLOW + " _   _      _ _       ")
    print( "| | | | ___| | | ___ ")
    print( '| |_| |/ _ \ | |/ _ \ ')
    print( '|  _  |  __/ | | (_) | ')
    print('|_| |_|\___|_|_|\___/ ')
        
    print("WELCOME TO THE DUNGEON!")
    name = input("What is your name? ")

    start_location = (20, 10)
    while True:
        avatar = input('''Select an avatar!
        1. "\U0001F63A"
        2. "\U0001F61C"
        3. "\U0001F60E"
        4. "\U0001F9DA"
        5. "\U0001F435"
        >> ''')
        if avatar == '1':
            player = Human(name, start_location,'\U0001F63A' )
            break
        elif avatar == '2':
            player = Human(name, start_location,'\U0001F61C' )
            break
        elif avatar == '3':
            player = Human(name, start_location,'\U0001F60E' )
            break
        elif avatar == '4':
            player = Human(name, start_location,'\U0001F9DA' )
            break
        elif avatar == '5':
            player = Human(name, start_location,'\U0001F435' )
            break
        else:
            print("Please insert a valid input.")
    
    
    gnome_location = (10, 10)
    gnome = Gnome("G", gnome_location, None, '\U0001F47E')
    gnome2_location = (5, 10)
    gnome2 = Gnome("G2", gnome2_location, None, '\U0001F479')
  
    
    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).
    
    pick = PickAxe('pickaxe', '\U0001FA93')
    
    pickaxe_location_candidate = dungeon.find_free_tile()

    while not dungeon.are_connected(player.loc(), pickaxe_location_candidate):
        pickaxe_location_candidate = dungeon.find_free_tile()            
    
    dungeon.add_item(player, pick, 1, xy=pickaxe_location_candidate)

    #Creacion de distintos items que se generan en el mapa
    sword = Sword('sword', '\U0001F5E1', 10, 50)
    dungeon.add_item(player, sword, 2)
    amulet = Amulet('amulet', '\U0001F4B0')
    dungeon.add_item(player, amulet, 3)
    food = Food('food', '\U0001F355')
    dungeon.add_item(player, food, 2)
    items_picked_up = []
    turns = 0

    
    start = False
    while not start:
        option = input('1. Read instructions\n2. Start game\nInsert an input please> ')
        if option == '1':
            print('''THE GAME IS SIMPLE.
            The goal is to move your character through the map in order to reach the third level where you will have
            to collect the treassure. Use the keys w, a, s, d to move. 
            You can also use the p to pick up items and the space bar to ascend or descend stairs. Make sure you collect the pick before
            you descend the stairs. If you don't, you won't be able to go to the next level.
            BE CAREFUL! There are gnomes you will have to fight in each level. Collect the pickaxe before you fight them.
            Win the game by getting back to level 0 with the treassure and by having collected any and every other object found. 
            GOOD LUCK!!''')
        elif option == '2':
            start = True
            print(Fore.BLUE +'Good luck soldier!')
            print(Back.WHITE)      


    while dungeon.level >= 0:
        turns += 1
        # render map
        
        
        dungeon.render(player, gnome, gnome2)
        print("""Type 'q' to quit. Move with the keys w, a, s, d. Pick up items with the p key. 
        Use the space bar to ascend or descend stairs.""")
        
        # get player input
        key = read_single_keypress() 
        if key == 'q':
            print(Style.RESET_ALL)
            print("Thanks for playing! See you next time :)")
            break

        # move player
        actions.move_to(dungeon, player, player.loc(), key, items_picked_up, gnome, gnome2)
        actions.attack(dungeon, player, gnome, items_picked_up)
        gnome_actions.gnome_movements(dungeon, player, gnome, gnome2)
        if dungeon.level == 2:
            actions.attack(dungeon, player, gnome2, items_picked_up)
            actions.attack(dungeon, player, gnome, items_picked_up)
        
        if player.hp <=0:
            print(Style.RESET_ALL)
            print(Fore.RED +"Oh, no! You have run out of health points. You lost the game :(")
            print('  _______ _______     __           _____          _____ _   _ ')
            print(" |__   __|  __ \ \   / /     /\   / ____|   /\   |_   _| \ | |")
            print('    | |  | |__) \ \_/ /     /  \ | |  __   /  \    | | |  \| |')
            print('    | |  |  _  / \   /     / /\ \| | |_ | / /\ \   | | |   ` |')
            print('    | |  | | \ \  | |     / ____ \ |__| |/ ____ \ _| |_| |\  |')
            print('    |_|  |_|  \_\_| |_   /_/    \_\_____/_/    \_\_____|_| \_|')
            print(Style.RESET_ALL)
            break
        
        if dungeon.level == 0 and len(items_picked_up) >= 4:
            print(Style.RESET_ALL)
            print(Fore.GREEN + "You have picked up the treassure and made it back to the start!")
            print("CONGRATULATIONS, YOU WON!")
            print("You have completed the game in", turns, "moves!")
            print(' __          _______ _   _ _   _ ______ _____')
            print(' \ \        / /_   _| \ | | \ | |  ____|  __ \ ')
            print('  \ \  /\  / /  | | |  \| |  \| | |__  | |__) |')
            print('   \ \/  \/ /   | | | . ` | . ` |  __| |  _  / ')
            print('    \  /\  /   _| |_| |\  | |\  | |____| | \ \ ')
            print('     \/  \/   |_____|_| \_|_| \_|______|_|  \_\ ')
            print(Style.RESET_ALL)
            break
       
       


    # Salió del loop principal, termina el juego
