def solution():
    # Calculate the total number of plants in the garden
    total_plants = 20 * 10

    # Calculate the number of plants used for parsley and rosemary
    parsley_plants = 3 * 10
    rosemary_plants = 2 * 10
    used_plants = parsley_plants + rosemary_plants

    # Calculate the number of chive plants
    chive_plants = total_plants - used_plants
    result = chive_plants
    return result

print(solution())