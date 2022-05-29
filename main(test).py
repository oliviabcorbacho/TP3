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
    
