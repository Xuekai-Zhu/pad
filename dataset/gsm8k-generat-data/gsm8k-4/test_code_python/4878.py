def solution():
    """Bugs are thriving in a garden of 30 plants. The bugs are very hungry today and completely ate 20 plants. The next day, they were still full and only ate half of the remaining plants. After that, they ate only 1 of the plants that were left. How many plants remain?"""
    # Define the initial number of plants
    total_plants = 30

    # Calculate the number of plants left after the first day
    remaining_plants = total_plants - 20

    # Calculate the number of plants left after the second day
    remaining_plants = remaining_plants / 2

    # Calculate the number of plants left after the third day
    remaining_plants -= 1

    # Return the result
    result = remaining_plants
    return result

print(solution())