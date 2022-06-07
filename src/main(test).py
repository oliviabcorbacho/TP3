from player import Player

if __name__ == '__main__':
    xy = [0,0]
    player = Player('Player1', xy)
# recibir evento del teclado
#moverse
    xy[0] += 1
    xy[1] += 1

    player.move_to(xy)

    print(player.loc())

    print(player.hp)

    player.hp = 10

    print(player.hp)
    
#%%
items_picked_up = [' item pickaxe', 'hope']

if "pickaxe" in items_picked_up:
    print('yes')
else:
    print('not')
# %%
import pygame as pg

# %%
from colorama import Fore, Back, Style
print(Fore.RED + " _   _      _ _       ")
print(Fore.RED + "| | | | ___| | | ___ ")
print(Fore.RED + '| |_| |/ _ \ | |/ _ \ ')
print(Fore.RED + '|  _  |  __/ | | (_) | ')
print(Fore.RED + '|_| |_|\___|_|_|\___/ ')

print(Fore.BLUE + "hello")
# %%
