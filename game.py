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

"""
import pygame
pygame.mixer.init()
crash_sound = pygame.mixer.Sound("Monkeys-Spinning-Monkeys.mp3")
crash_sound.play()"""





ROWS = 25
COLUMNS = 80


if __name__ == "__main__":
    # initial parameters
    #level = 0
   # initial locations may be random generated

    name = input("What is your name? ")
    start_location = (20, 10)
    player = Human(name, start_location )
    print('player ')
    gnome_location = (10, 10)
    gnome = Gnome("G", gnome_location)
    print('gnome ')
    gnome2_location = (5, 10)
    gnome2 = Gnome("G2", gnome2_location, None, '&')
    gnome3_location = (20, 20)
    gnome3 = Gnome("G3", gnome3_location, None, '§')
    print('gnome2 ')
    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).
    print('dungeon')
    pick = PickAxe('pickaxe', '(')
    dungeon.add_item(player, pick, 1)
    print('picj')
    sword = Sword('sword', '/', 10, 50)
    dungeon.add_item(player, sword, 2)
    print('sword') #aca hay un bug pq se suele colgar en este punto
    amulet = Amulet('amulet', '"')
    dungeon.add_item(player, amulet, 3)
    print('amulet')
    food = Food('food', '¤')
    dungeon.add_item(player, food, 2)
    print('items')
    items_picked_up = []
    turns = 0

    print("WELCOME TO THE DUNGEON!")
    start = False
    while not start:
        option = input('1. Read instructions\n2. Start game\nInsert an input please> ')
        if option == '1':
            print('''THE GAME IS SIMPLE.
            The goal is to move your character, @, through the map in order to reach the third level where you will have
            to collect the treassure '"' before using the down stairs, <, to descend. Use the keys w, a, s, d to move. 
            You can also use the p to pick up items and the space bar to ascend or descend stairs. There will also be gnomes in the game
            (G, § and &) who can damage your hit points if you do not have the propper weapons (pickaxe, '(' and sword, '/'). Collect the food,
            ¤, to restore your hit points. 
            Win the game by getting back to level 0 with the treassure and by having collected any and every other object found ('(', '/','¤', '"')). 
            GOOD LUCK!!''')
        elif option == '2':
            start = True
            print('Good luck soldier!')


    while dungeon.level >= 0:
        turns += 1
        # render map
        
        
        dungeon.render(player, gnome, gnome2)
        
        # get player input
        key = read_single_keypress() 
        if key == 'q':
            print("Thanks for playing! See you next time :)")
            break

        # move player
        actions.move_to(dungeon, player, player.loc(), key, items_picked_up, gnome, gnome2)
        actions.attack(dungeon, player, gnome, items_picked_up)
        gnome_actions.gnome_movements(dungeon, player, gnome, gnome2)
        if dungeon.level == 2:
            actions.attack(dungeon, player, gnome2, items_picked_up)
            actions.attack(dungeon, player, gnome3, items_picked_up)
        
        if dungeon.level == 0 and len(items_picked_up) >= 4:
            print("You have picked up the treassure and made it back to the start!")
            print("CONGRATULATIONS, YOU WON!")
            print("You have completed the game in", turns, "moves!")
            break
       
        print()
        
        

        if player.hp <=0:
            print("Uh, oh! You died! Better luck next time!")


    # Salió del loop principal, termina el juego
