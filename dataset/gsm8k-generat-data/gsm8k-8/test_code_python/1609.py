def solution():
    bottle_capacity = 4
    quarter_of_bottle = bottle_capacity / 4
    remaining_water = bottle_capacity - quarter_of_bottle
    drank_water = (2/3) * remaining_water
    remaining_water -= drank_water
    result = remaining_water
    return result

print(solution())