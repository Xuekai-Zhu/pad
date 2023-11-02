def solution():
    """Charley bought 30 pencils. She lost 6 pencils while moving to school, and of course, also lost 1/3 of the remaining pencils because she wasn't very good at keeping track of pencils. How many pencils does she currently have?"""
    initial_pencils = 30
    lost_pencils = 6
    remaining_pencils = initial_pencils - lost_pencils
    lost_again_pencils = remaining_pencils / 3
    current_pencils = remaining_pencils - lost_again_pencils
    result = current_pencils
    return result

print(solution())