#!/usr/bin/env python3
import time
import mapping
import msvcrt


import random
from human import Human
from items import Item, PickAxe, Sword, Amulet
from gnome import Gnome
import actions
from keys import read_single_keypress




ROWS = 25
COLUMNS = 80


if __name__ == "__main__":
    # initial parameters
    level = 0
    #start_position = mapping.Dungeon.get_stairs_up(level)
    #start_pos = (start_position[0] + 1, start_position[1])
   # mapping.Dungeon.is_free(start_pos)

    #initial_location = mapping.Dungeon.find_free_tile()
    #(random.randint(1, ROWS), random.randint(1, COLUMNS))
    name = input("What is your name? ")
    player = Human(name, (20, 22) )

    # initial locations may be random generated
    gnome = Gnome("G", (10,21))

    dungeon = mapping.Dungeon(ROWS, COLUMNS, 3)
    # Agregarle cosas al dungeon, cosas que no se creen automáticamente al crearlo (por ejemplo, ya se crearon las escaleras).

    pick = PickAxe('pickaxe', '(')
    dungeon.add_item(pick, 1)

    sword = Sword('sword', '/', 10, 50)
    dungeon.add_item(sword, 1)

    items_picked_up = []
    turns = 0

 
    while dungeon.level >= 0:
        turns += 1
        # render map
        
        
        dungeon.render(player, gnome)
        
        # get player input
        key = read_single_keypress() 
        if key == 'q':
            print("Thanks for playing! See you next time :)")
            break

        # move player
        actions.move_to(dungeon, player, player.loc(), key, items_picked_up)
        actions.climb_stair(dungeon, player, player.loc(), key)
        actions.descend_stair(dungeon, player, player.loc(), key)
        actions.pickup(dungeon, player, key, items_picked_up)
        actions.attack(dungeon, player, gnome, items_picked_up)
        print()
        
        

        if player.hp <=0:
            print("Uh, oh! You died! Better luck next time!")


    # Salió del loop principal, termina el juego
