def solution():
    """A garden produced 237 potatoes, 60 less cucumbers and twice as many peppers as the cucumbers. How many vegetables did the garden produce?"""
    potatoes = 237
    cucumbers = potatoes - 60
    peppers = cucumbers * 2
    total_veggies = potatoes + cucumbers + peppers
    result = total_veggies
    return result

print(solution())