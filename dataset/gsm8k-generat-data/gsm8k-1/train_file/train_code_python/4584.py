def solution():
    """How many portions of 200 ml milk can Jasmine pour from a full 2-liter container of milk?"""
    full_container = 2000 #2 liters converted to milliliters
    portion_size = 200
    portions_possible = full_container // portion_size
    result = portions_possible
    return result

print(solution())