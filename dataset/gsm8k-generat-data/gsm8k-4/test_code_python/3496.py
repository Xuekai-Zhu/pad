def solution():
    """A farmer planted 30 rows of tomatoes with 10 plants in each row. Each tomato plant yields 20 pieces of tomatoes. How many pieces of tomatoes can the farmer get from all his planted tomatoes?"""
    # Define the number of rows and plants per row
    rows = 30
    plants_per_row = 10

    # Define the yield per plant
    yield_per_plant = 20

    # Calculate the total number of tomato plants
    total_plants = rows * plants_per_row

    # Calculate the total number of tomatoes
    total_tomatoes = total_plants * yield_per_plant

    # return the result
    result = total_tomatoes
    return result

print(solution())