import msvcrt
import random
from re import X

def read_single_keypress():
            key= msvcrt.getch().decode('UTF-8')
            return key



def random_location(ROWS, COLUMNS):
    x = (random.randint(1, ROWS), random.randint(1, COLUMNS))
    this_works = False
    while not this_works:
        if mapping.Dungeon.is_connected(x, PICO):
            this_works = True
        else:
            x = (random.randint(1, ROWS), random.randint(1, COLUMNS))
    return x




