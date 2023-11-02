def solution():
    
    total_rooms = 10
    green_rooms = int(3/5 * total_rooms)
    purple_rooms = total_rooms - green_rooms
    walls_per_room = 8
    purple_walls = purple_rooms * walls_per_room
    result = purple_walls
    return result

print(solution())