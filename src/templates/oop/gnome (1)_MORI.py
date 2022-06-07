import random
from player import Player
import mapping

class Gnome(Player):
    def __init__(self, name, xy,weapon=None, face='G', hit_points=50):
        super().__init__(name, xy, face,weapon=weapon, hit_points=hit_points)
    
    def damage(self):
        return self._damage(10)

    def move(self, dungeon, player):
        if dungeon.level == 0:
            self.level_cero_movement(dungeon, player)
        elif dungeon.level ==1:
            self.level_one_movement(dungeon, player)
        else:
            self.level_two_movement(dungeon, player)
        return False
    

    def level_cero_movement(self, dungeon, player):
        x,y = self.loc()
        key = random.choice(['w', 's', 'a', 'd'])
        if key =='w':
            self.move_up(dungeon, x, y)
        elif key == 's':
            self.move_down(dungeon, x, y)
        elif key == 'd':
            self.move_right(dungeon, x, y)
        elif key =='a':
             self.move_left(dungeon, x, y)

    def level_one_movement(self, dungeon, player):
        x,y = self.loc()
        xp, yp = player.loc()
        x_dif = abs(x-xp)
        y_dif = abs(y-yp)
        if x == xp:
            if y-yp > 0:
                self.move_up(dungeon, x, y)
            else:
                self.move_down(dungeon, x, y)
        elif y == yp:
            if x-xp > 0:
                self.move_left(dungeon, x, y)
            else:
                self.move_right(dungeon, x, y)
        else: 
            if x_dif < y_dif:
                if x-xp > 0:
                    self.move_left(dungeon, x, y)
                else:
                    self.move_right(dungeon, x, y)
            else:
                if y-yp > 0:
                    self.move_up(dungeon, x, y)
                else:
                    self.move_down(dungeon, x, y)
    
    def level_two_movement(self, dungeon, player):
        x,y = self.loc()
        xp, yp = player.loc()
        x_dif = abs(x-xp)
        y_dif = abs(y-yp)
        if x == xp:
            if y-yp > 0:
                self.move_up(dungeon, x, y-1)
            else:
                self.move_down(dungeon, x, y+1)
        elif y == yp:
            if x-xp > 0:
                self.move_left(dungeon, x-1, y)
            else:
                self.move_right(dungeon, x+1, y)
        else:
            if x_dif < y_dif:
                if x-xp > 0:
                    self.move_left(dungeon, x-1, y)
                else:
                    self.move_right(dungeon, x+1, y)
            else:
                if y-yp > 0:
                    self.move_up(dungeon, x, y-1)
                else:
                    self.move_down(dungeon, x, y+1)

    def move_up(self, dungeon, x, y):
        if dungeon.loc((x,y-1)).is_walkable() and y-1 >=0:
                self.move_to((x,y-1))
    
    def move_down(self, dungeon, x, y):
        if dungeon.loc((x,y+1)).is_walkable() and y +1 <= dungeon.rows:
            self.move_to((x,y+1))
    
    def move_left(self, dungeon, x, y):
        if dungeon.loc((x-1,y)).is_walkable() and x-1 >= 0:
            self.move_to((x-1,y))
    
    def move_right(self, dungeon, x, y):
        if dungeon.loc((x+1,y)).is_walkable() and x+1 <= dungeon.columns:
            self.move_to((x+1,y))