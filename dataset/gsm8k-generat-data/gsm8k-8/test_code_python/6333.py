def solution():
    # Define the initial plant counts
    ferns = 3
    palms = 5
    succulents = 7

    # Calculate the total number of plants
    total_plants = ferns + palms + succulents

    # Calculate the number of additional plants needed to reach 24
    additional_plants = 24 - total_plants
    result = additional_plants
    return result

print(solution())