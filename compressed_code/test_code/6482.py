def solution():
    
    living_room_walls = 600
    bedroom_walls = 3 * 400
    total_walls = living_room_walls + bedroom_walls
    square_feet_per_gallon = 600
    gallons_of_paint = total_walls / square_feet_per_gallon
    result = gallons_of_paint
    return result

print(solution())