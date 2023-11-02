def solution():
    living_room_area = 600
    bedroom_area = 400
    num_bedrooms = 3
    area_to_paint = living_room_area + (bedroom_area * num_bedrooms)
    square_feet_per_gallon = 600
    num_gallons_needed = area_to_paint / square_feet_per_gallon
    result = num_gallons_needed
    return result

print(solution())