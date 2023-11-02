def solution():
    # Calculate the number of parking spaces on each level
    level1_spaces = 90
    level2_spaces = level1_spaces + 8
    level3_spaces = level2_spaces + 12
    level4_spaces = level3_spaces - 9

    # Calculate the total number of parking spaces
    total_spaces = level1_spaces + level2_spaces + level3_spaces + level4_spaces

    # Calculate the number of available parking spaces
    num_available = total_spaces - 100

    result = num_available
    return result

print(solution())