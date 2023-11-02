def solution():
    # Find the total number of walls in the house
    total_walls = 10 * 8  

    # Find the number of rooms painted green
    green_rooms = int((3/5) * 10)  

    # Find the number of walls in green rooms
    green_walls = green_rooms * 8  

    # Find the number of walls painted purple
    purple_walls = total_walls - green_walls
    result = purple_walls
    return result

print(solution())