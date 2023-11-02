def solution():
    # Let x be the number of floors in building B
    # Then building A has x - 9 floors
    # And building C has 5x - 6 floors
    x = 4 + 9  # Number of floors in Building B

    # Calculate the number of floors in Building C
    num_floors_building_c = 5*x - 6

    result = num_floors_building_c
    return result

print(solution())