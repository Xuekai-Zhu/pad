def solution():
    """A garden produced 237 potatoes, 60 fewer cucumbers and twice as many peppers than the cucumbers. How many vegetables did the garden produce?"""
    potatoes = 237
    cucumbers = potatoes - 60
    peppers = cucumbers * 2
    total_veggies = potatoes + cucumbers + peppers
    result = total_veggies
    return result

print(solution())