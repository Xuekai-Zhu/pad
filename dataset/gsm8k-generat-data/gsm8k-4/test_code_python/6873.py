def solution():
    """Betty’s herb garden has 2 more than twice as many oregano plants as basil. If there are 5 basil plants, what is the total number of plants in the garden?"""
    # Define the number of basil plants
    basil_plants = 5

    # Calculate the number of oregano plants
    oregano_plants = 2 + 2 * basil_plants

    # Calculate the total number of plants
    total_plants = basil_plants + oregano_plants

    # return the result
    result = total_plants
    return result

print(solution())