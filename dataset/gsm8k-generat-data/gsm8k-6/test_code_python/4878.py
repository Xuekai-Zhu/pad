def solution():
    # Calculate the number of plants remaining after the bugs ate 20 plants
    remaining_plants = 30 - 20  # the bugs ate 20 of the 30 plants
    # Calculate the number of plants remaining after the bugs ate half of the remaining plants
    remaining_plants = remaining_plants / 2  
    # Calculate the number of plants remaining after the bugs ate 1 more plant
    remaining_plants = remaining_plants - 1  
    result = remaining_plants
    return result

print(solution())