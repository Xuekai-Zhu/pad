def solution():
    """A farmer planted 30 rows of tomatoes with 10 plants in each row.
    Each tomato plant yields 20 pieces of tomatoes.
    How many pieces of tomatoes can the farmer get from all his planted tomatoes?"""
    # Define the number of rows and plants per row
    rows = 30
    plants_per_row = 10

    # Calculate the total number of plants
    total_plants = rows * plants_per_row

    # Calculate the total number of tomatoes
    tomatoes = total_plants * 20

    # Display the total number of tomatoes
    result = tomatoes
    return result

print(solution())