def solution():
    """A pet store currently has 5 dogs, 2 cats, and 10 birds. How many legs in total do the pets in the store have?"""
    dogs_legs = 4 * 5
    cats_legs = 4 * 2
    birds_legs = 2 * 10
    total_legs = dogs_legs + cats_legs + birds_legs
    result = total_legs
    return result

print(solution())