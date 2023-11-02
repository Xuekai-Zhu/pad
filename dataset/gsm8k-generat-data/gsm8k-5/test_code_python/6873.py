def solution():
    basil_plants = 5  # Given that there are 5 basil plants
    oregano_plants = (2 + 2 * basil_plants)  # Calculate number of oregano plants

    # Calculate total number of plants in the garden
    total_plants = basil_plants + oregano_plants
    result = total_plants
    return result

print(solution())