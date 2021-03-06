import random

class Player:
    def __init__(self, name, xy, face, weapon =None,  hit_points=50):
        self.name = name
        self.x, self.y = xy
        self._hp = hit_points
        self.max_hp = hit_points

        self.alive = True
        self.face = face
        self.weapon = weapon
    
    @property 
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        if value> self.max_hp:
            self._hp = self.max_hp
        else:
            self._hp = value
        
    def loc(self):
        return self.x, self.y


    def move_to(self, xy):
        self.x, self.y = xy

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Player('{self.name}', '{self.loc}', '{self.hp}')"
    
    
    def kill(self):
        self.hp = 0
        self.alive = False


    def _damage(self, dmg):
        if self.weapon:
            return random.random() * dmg * 2 + 5
        return random.random() * dmg + 1