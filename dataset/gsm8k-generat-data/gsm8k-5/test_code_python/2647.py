def solution():
    boa_constrictors = 40
    pythons = 3 * boa_constrictors
    total_snakes = boa_constrictors + pythons + 0  # add 0 for the rattlesnakes
    rattlesnakes = 200 - total_snakes
    result = rattlesnakes
    return result

print(solution())