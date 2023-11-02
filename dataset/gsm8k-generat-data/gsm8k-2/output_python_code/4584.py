def solution():
    """How many portions of 200 ml milk can Jasmine pour from a full 2-liter container of milk?"""
    full_milk = 2000
    portion_size = 200
    portions = full_milk // portion_size
    result = portions
    return result

print(solution())