def solution():
    
    total_rooms = 10
    walls_per_room = 8
    green_rooms = (3/5) * total_rooms
    purple_rooms = total_rooms - green_rooms
    purple_walls = purple_rooms * walls_per_room
    result = purple_walls
    return result

print(solution())