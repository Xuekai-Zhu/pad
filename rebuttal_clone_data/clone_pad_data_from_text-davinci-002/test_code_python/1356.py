def solution():
    num_rooms = 10
    walls_per_room = 8
    rooms_painted_green = num_rooms * (3/5)
    rooms_painted_purple = num_rooms - rooms_painted_green
    total_walls_painted_purple =  rooms_painted_purple * walls_per_room
    result = total_walls_painted_purple
    return result

print(solution())