def solution():
    # Calculate the total number of soda cases needed to build a pyramid that's four levels tall
    level_1 = 1
    level_2 = 2**2
    level_3 = 3**2
    level_4 = 4**2
    total_cases = level_1 + level_2 + level_3 + level_4
    result = total_cases
    return result

print(solution())