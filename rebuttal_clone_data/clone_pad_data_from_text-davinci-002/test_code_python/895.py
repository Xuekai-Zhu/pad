def solution():
    living_room_size = 600
    bedroom_size = 400
    num_bedrooms = 3
    total_wall_space = living_room_size + (num_bedrooms * bedroom_size)
    paint_coverage = 600
    num_gallons = total_wall_space / paint_coverage
    result = num_gallons
    return result

print(solution())