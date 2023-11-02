def solution():
    """Henrietta is repainting her house. The walls in the living room take up 600 square feet. She has three bedrooms. The walls in each bedroom take up 400 square feet. If one gallon of paint can cover 600 square feet, how many gallons of paint does Henrietta need to paint her house?"""
    living_room_size = 600
    bedroom_size = 400
    total_bedroom_size = bedroom_size * 3
    total_wall_size = living_room_size + total_bedroom_size
    gallons_needed = total_wall_size / 600
    result = gallons_needed
    return result

print(solution())