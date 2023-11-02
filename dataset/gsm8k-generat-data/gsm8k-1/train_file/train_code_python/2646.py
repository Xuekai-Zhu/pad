def solution():
    """There are 200 snakes in a park. There are three times as many pythons as boa constrictors. If there 40 boa constrictors and the rest of the snakes are rattlesnakes, calculate the total number of rattlesnakes in the park."""
    total_snakes = 200
    boa_constrictors = 40
    pythons = 3 * boa_constrictors
    rattlesnakes = total_snakes - (boa_constrictors + pythons)
    result = rattlesnakes
    return result

print(solution())