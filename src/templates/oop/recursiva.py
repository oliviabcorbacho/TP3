#connected is a recursive function that returns True if two elements on the map are connected. It returns False if they are not.

def connected(initial, end):
    if initial == end:
        return True
    x, y = initial

    possibles = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for location in possibles:
        if 0 <= location[0]<= columns and 0 <= location[1]<= rows:
            if location == end:
                return True
            elif location is walkable:
                return connected(location, end)
            elif location in visited:
                return False
            else:
                return False

        return False
