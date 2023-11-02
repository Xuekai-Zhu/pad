def solution():
    
    dining_room_walls = 4
    living_room_walls = 4
    time_per_wall = 2
    total_time = time_per_wall * (dining_room_walls + living_room_walls - 1)
    result = total_time
    return result

print(solution())