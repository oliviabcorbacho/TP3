from typing import Union


import mapping
import player
import gnome


numeric = Union[int, float]


def clip(value: numeric, minimum: numeric, maximum: numeric) -> numeric:
    if value < minimum:
        return minimum
    if value > maximum:
        return maximum
    return value


def attack(dungeon, player, gnome): #esto va a hacer que el gnome ataque al player
    
    raise NotImplementedError


def move_to(dungeon: mapping.Dungeon, player: player.Player, location: tuple[numeric, numeric], key:str):
    x,y = location
    try: 
        if key =='w':
            move_up(dungeon, player, x, y)
        elif key == 's':
            move_down(dungeon, player, x, y)
        elif key == 'd':
            move_right(dungeon, player, x, y)
        elif key =='a':
            move_left(dungeon, player, x, y)

        elif key == ' ':
            if dungeon.loc((x,y)).get_face() == '>':
                descend_stair(dungeon, player)
            elif dungeon.loc((x,y)).get_face() == '<':
                climb_stair(dungeon, player)

    except AttributeError:
        pass


def move_up(dungeon: mapping.Dungeon, player: player.Player, x, y):
    if dungeon.loc((x,y-1)).is_walkable() and y-1 >=0:
                player.move_to((x,y-1))
def move_down(dungeon: mapping.Dungeon, player: player.Player, x, y):
    if dungeon.loc((x,y+1)).is_walkable() and y +1 <= dungeon.rows:
                player.move_to((x,y+1))
def move_left(dungeon: mapping.Dungeon, player: player.Player, x, y):
    if dungeon.loc((x-1,y)).is_walkable() and x-1 >= 0:
                player.move_to((x-1,y))
def move_right(dungeon: mapping.Dungeon, player: player.Player, x, y):
    if dungeon.loc((x+1,y)).is_walkable() and x+1 <= dungeon.columns:
                player.move_to((x+1,y))


def climb_stair(dungeon: mapping.Dungeon, player: player.Player):
    dungeon.level += 1
    player.loc = dungeon.get_stairs_down(dungeon.level) #completar


def descend_stair(dungeon: mapping.Dungeon, player: player.Player):

    dungeon.level -= 1
    player.loc = dungeon.get_stairs_up(dungeon.level) #completar
    

def pickup(dungeon: mapping.Dungeon, player: player.Player, location: tuple[numeric, numeric]):
    x, y = location
    if dungeon.loc((x, y)) == '/':
        player.weapon = '/'
        dungeon.loc((x, y)).set_face(' ')
    
    #elif dungeon.loc((x, y)) == 
    raise NotImplementedError
