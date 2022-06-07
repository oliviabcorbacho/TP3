from typing import Union


import mapping
import player
import gnome
import foods
from human import Human
from colorama import Fore, Back, Style


numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

def attack(dungeon: mapping.Dungeon, player: player.Player, gnome: gnome.Gnome, items_picked_up ): #esto va a hacer que el gnome ataque al player
    '''This function represents what happens when teh player attacks the gnome or vice versa. If the list called items_picked_up
    has two or more elements, it means that the player has picked up the pickake and the sword, meaning it can cause damage to the gnome.
    If the list has less than two items, it means the sword has not been picked up yet, so the player cannot cause damage to the gnome, 
    and instead, if it crosses the gnome, the gnome will attack the player.'''

    try: 
        if player.loc() == gnome.loc() and len(items_picked_up) >=2:
            gnome.hp -= player.damage()
            if gnome.hp <= 0:
                gnome.kill()
            print(gnome.hp)
        elif player.loc() == gnome.loc() and len(items_picked_up) < 2:
            player.hp -= gnome.damage()   

    except NotImplementedError:
        pass


def move_to(dungeon: mapping.Dungeon, player: player.Player, location: tuple[numeric, numeric], key:str, items_picked_up, gnome: gnome.Gnome, gnome2: gnome.Gnome):
    '''This function represents what happens when the player moves to a new location. It checks if the player is trying to move to a location'''
    x,y = location
    try: 
        if key =='w':
            move_up(dungeon, player, x, y, items_picked_up)
        elif key == 's':
            move_down(dungeon, player, x, y, items_picked_up)
        elif key == 'd':
            move_right(dungeon, player, x, y, items_picked_up)
        elif key =='a':
            move_left(dungeon, player, x, y, items_picked_up)

        elif key == ' ':
            if dungeon.loc((x, y)).get_face() == '>':
                print("You have descended the stairs")
                descend_stair(dungeon, player, items_picked_up)
            elif dungeon.loc((x, y)).get_face() == '<':
                print("You have climbed the stairs")
                climb_stair(dungeon, player)

        elif key == 'p':
            pickup(dungeon, player, items_picked_up)


    except AttributeError:
        pass


def move_up(dungeon: mapping.Dungeon, player: player.Player, x, y, items_picked_up):
    '''This function makes the player move up if the location is walkable.'''
    
    if dungeon.loc((x,y-1)).is_walkable() and y-1 >=0:
                player.move_to((x,y-1))
    elif len(items_picked_up) !=0 and y-1 >=0:
        player.move_to((x, y-1))
        dungeon.dig(player.loc())

def move_down(dungeon: mapping.Dungeon, player: player.Player, x, y, items_picked_up):
    '''This function makes the player move down if the location is walkable.'''
    
    if dungeon.loc((x,y+1)).is_walkable() and y +1 <= dungeon.rows:
                player.move_to((x,y+1))
    elif len(items_picked_up) != 0 and y+1 >=0:
        player.move_to((x, y+1))
        dungeon.dig(player.loc())

def move_left(dungeon: mapping.Dungeon, player: player.Player, x, y, items_picked_up):
    '''This function makes the player move left if the location is walkable.'''
    
    if dungeon.loc((x-1,y)).is_walkable() and x-1 >= 0:
                player.move_to((x-1,y))
    elif len(items_picked_up) != 0 and x-1 >=0:
        player.move_to((x-1,y))
        dungeon.dig(player.loc())

def move_right(dungeon: mapping.Dungeon, player: player.Player, x, y, items_picked_up):
    '''This function makes the player move right if the location is walkable.'''
    
    if dungeon.loc((x+1,y)).is_walkable() and x+1 <= dungeon.columns:
                player.move_to((x+1,y))
    elif len(items_picked_up) !=0 and x+1 >=0:
        player.move_to((x+1, y))
        dungeon.dig(player.loc())


def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    '''This function allows the player to climb the staris and go to the next level.'''
    dungeon.climb_level()

def descend_stair(dungeon: mapping.Dungeon, player: player.Player, items_picked_up):
    '''This function allows the player to descend the staris and go to the previous level.'''
    if len(items_picked_up) >= 1:
        dungeon.descend_level()
    

def pickup(dungeon: mapping.Dungeon, player: player.Player, items_picked_up):
    try:
            my_items = dungeon.get_items(player.loc())
            for item in my_items:
                items_picked_up.append(item)
                if item.type == 'weapon':
                    player.weapon = item
                elif item.type == 'food':
                    if player.hp + 10 <= player.max_hp:
                        player.hp += 10
                        
                    else:
                        player.hp = player.max_hp
                elif item.type == 'tool':
                    player.tool = item
                
            
    except AttributeError:
        pass
