def solution():
    """Charley bought 30 pencils. She lost 6 pencils while moving to school, and of course, also lost 1/3 of the remaining pencils because she wasn't very good at keeping track of pencils. How many pencils does she currently have?"""
    initial_pencils = 30
    lost_pencils_moving = 6
    remaining_pencils_after_move = initial_pencils - lost_pencils_moving
    lost_fraction = 1/3
    lost_pencils = lost_fraction * remaining_pencils_after_move
    remaining_pencils = remaining_pencils_after_move - lost_pencils
    result = remaining_pencils
    return result

print(solution())