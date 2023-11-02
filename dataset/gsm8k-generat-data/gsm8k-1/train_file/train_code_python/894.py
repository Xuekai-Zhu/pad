def solution():
    """Henrietta is repainting her house. The walls in the living room take up 600 square feet. She has three bedrooms. The walls in each bedroom take up 400 square feet. If one gallon of paint can cover 600 square feet, how many gallons of paint does Henrietta need to paint her house?"""
    living_room_walls = 600
    bedroom_walls = 3 * 400
    total_walls = living_room_walls + bedroom_walls
    square_feet_per_gallon = 600
    gallons_of_paint = total_walls / square_feet_per_gallon
    result = gallons_of_paint
    return result

print(solution())