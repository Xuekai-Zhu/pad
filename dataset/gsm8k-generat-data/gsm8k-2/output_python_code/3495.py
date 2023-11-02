def solution():
    """A farmer planted 30 rows of tomatoes with 10 plants in each row. Each tomato plant yields 20 pieces of tomatoes. How many pieces of tomatoes can the farmer get from all his planted tomatoes?"""
    rows = 30
    plants_per_row = 10
    yield_per_plant = 20
    total_tomatoes = rows * plants_per_row * yield_per_plant
    result = total_tomatoes
    return result

print(solution())