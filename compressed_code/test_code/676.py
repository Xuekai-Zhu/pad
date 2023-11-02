def solution():
    
    living_room_size = 600
    bedroom_size = 400
    total_bedroom_size = bedroom_size * 3
    total_wall_size = living_room_size + total_bedroom_size
    gallons_needed = total_wall_size / 600
    result = gallons_needed
    return result

print(solution())