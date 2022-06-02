from typing import Union


import mapping
import player
import gnome
import foods
from human import Human


numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value

#Hay que hacer que el jugador no pase del primer nivel sin juntar primero el pico

def attack(dungeon: mapping.Dungeon, player: player.Player, gnome: gnome.Gnome, items_picked_up ): #esto va a hacer que el gnome ataque al player
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


def move_to(dungeon: mapping.Dungeon, player: player.Player, location: tuple[numeric, numeric], key:str, items_picked_up):
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

    except AttributeError:
        pass


def move_up(dungeon: mapping.Dungeon, player: player.Player, x, y, items_picked_up):
    if dungeon.loc((x,y-1)).is_walkable() and y-1 >=0:
                player.move_to((x,y-1))
    elif len(items_picked_up) !=0 and y-1 >=0:
        player.move_to((x, y-1))
        dungeon.dig(player.loc())

def move_down(dungeon: mapping.Dungeon, player: player.Player, x, y, items_picked_up):
    if dungeon.loc((x,y+1)).is_walkable() and y +1 <= dungeon.rows:
                player.move_to((x,y+1))
    elif len(items_picked_up) != 0 and y+1 >=0:
        player.move_to((x, y+1))
        dungeon.dig(player.loc())

def move_left(dungeon: mapping.Dungeon, player: player.Player, x, y, items_picked_up):
    if dungeon.loc((x-1,y)).is_walkable() and x-1 >= 0:
                player.move_to((x-1,y))
    elif len(items_picked_up) != 0 and x-1 >=0:
        player.move_to((x-1,y))
        dungeon.dig(player.loc())

def move_right(dungeon: mapping.Dungeon, player: player.Player, x, y, items_picked_up):
    if dungeon.loc((x+1,y)).is_walkable() and x+1 <= dungeon.columns:
                player.move_to((x+1,y))
    elif len(items_picked_up) !=0 and x+1 >=0:
        player.move_to((x+1, y))
        dungeon.dig(player.loc())


def climb_stair(dungeon: mapping.Dungeon, player: player.Player, location, key):
    x, y = location
    try:
        if key == ' ' and dungeon.loc((x, y)).get_face() == '<':
            dungeon.level -= 1
            player.loc = dungeon.get_stairs_down(dungeon.level) #completar
    except AttributeError:
        pass

def descend_stair(dungeon: mapping.Dungeon, player: player.Player, location, key):
    x, y = location
    try: 
        if key == ' ' and dungeon.loc((x, y)).get_face() == '>':
            dungeon.level += 1
            player.loc = dungeon.get_stairs_up(dungeon.level)
    except AttributeError:
        pass
     #completar
    

def pickup(dungeon: mapping.Dungeon, player: player.Player, key, items_picked_up):
    try:
        if key == 'p':

            my_items = dungeon.get_items(player.loc())
            for item in my_items:
                items_picked_up.append(item)
                player.weapon = item
            
    except AttributeError:
        pass

def raise_hp(dungeon: mapping.Dungeon, player: player.Player, key):

    try:
        if key == 'e':
            dungeon.eat_foods(player.loc())
            if player.hp + 10 <= player.max_hp:
                player.hp += 10
            else:
                player.hp = player.max_hp
            
                
    except AttributeError:
        pass
