def solution():
    """Betty’s herb garden has 2 more than twice as many oregano plants as basil. If there are 5 basil plants, what is the total number of plants in the garden?"""
    basil_plants = 5
    oregano_plants = 2 + 2 * basil_plants
    total_plants = basil_plants + oregano_plants
    result = total_plants
    return result

print(solution())