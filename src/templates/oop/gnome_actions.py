import random
import mapping
import player
import gnome


def gnome_movements(dungeon: mapping.Dungeon, player: player.Player, gnome: gnome.Gnome, gnome2: gnome.Gnome):
    '''This function represents what happens when the gnome moves. It checks if the gnome is trying to move to a location'''
    if dungeon.level == 0:
        level_cero_movement(dungeon, gnome)
    elif dungeon.level ==1:
        level_one_movement(dungeon, gnome, player)
    else:
        level_two_movement(dungeon, gnome, player)
        level_two_movement(dungeon, gnome2, player)
    return False

def level_cero_movement( dungeon: mapping.Dungeon, gnome: gnome.Gnome):
        x, y = gnome.loc()
        key = random.choice(['w', 's', 'a', 'd'])
        if key =='w':
            move_up(dungeon, gnome, x, y)
        elif key == 's':
            move_down(dungeon, gnome, x, y)
        elif key == 'd':
            move_right(dungeon, gnome,  x, y)
        elif key =='a':
            move_left(dungeon, gnome, x, y)

def level_one_movement(dungeon: mapping.Dungeon, gnome: gnome.Gnome, player: player.Player):
        x,y = gnome.loc()
        xp, yp = player.loc()
        x_dif = abs(x-xp)
        y_dif = abs(y-yp)
        if x == xp:
            if y-yp > 0:
                move_up(dungeon, gnome, x, y)
            else:
                move_down(dungeon, gnome, x, y)
        elif y == yp:
            if x-xp > 0:
                move_left(dungeon, gnome, x, y)
            else:
                move_right(dungeon, gnome, x, y)
        else: 
            if x_dif < y_dif:
                if x-xp > 0:
                    move_left(dungeon, gnome, x, y)
                else:
                    move_right(dungeon, gnome, x, y)
            else:
                if y-yp > 0:
                    move_up(dungeon, gnome, x, y)
                else:
                    move_down(dungeon, gnome, x, y)
    
def level_two_movement(dungeon: mapping.Dungeon, gnome: gnome.Gnome, player: player.Player, ):
    x,y = gnome.loc()
    xp, yp = player.loc()
    x_dif = abs(x-xp)
    y_dif = abs(y-yp)
    if x == xp:
        if y-yp > 0:
            move_up(dungeon, gnome, x, y-1)
        else:
            move_down(dungeon,gnome, x, y+1)
    elif y == yp:
        if x-xp > 0:
            move_left(dungeon, gnome, x-1, y)
        else:
            move_right(dungeon, gnome, x+1, y)
    else:
        if x_dif < y_dif:
            if x-xp > 0:
                move_left(dungeon, gnome, x-1, y)
            else:
                move_right(dungeon, gnome, x+1, y)
        else:
            if y-yp > 0:
                move_up(dungeon, gnome, x, y-1)
            else:
                move_down(dungeon, gnome, x, y+1)

def move_up(dungeon: mapping.Dungeon, gnome: gnome.Gnome, x, y):
    if y-1 >=0:
        gnome.move_to((x,y-1))
    else:
        gnome.move_to((x,y))

def move_down(dungeon: mapping.Dungeon, gnome: gnome.Gnome, x, y):
    if y +1 <= dungeon.rows:
        gnome.move_to((x,y+1))
    else:
        gnome.move_to((x,y))

def move_left(dungeon: mapping.Dungeon, gnome: gnome.Gnome, x, y):
    if x-1 >= 0:
        gnome.move_to((x-1,y))
    else:
        gnome.move_to((x,y))

def move_right(dungeon: mapping.Dungeon, gnome: gnome.Gnome, x, y):
    if x+1 <= dungeon.columns:
        gnome.move_to((x+1,y))
    else:
        gnome.move_to((x,y))