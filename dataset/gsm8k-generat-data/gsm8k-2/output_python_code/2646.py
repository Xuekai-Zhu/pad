def solution():
    """There are 200 snakes in a park. There are three times as many pythons as boa constrictors. If there 40 boa constrictors and the rest of the snakes are rattlesnakes, calculate the total number of rattlesnakes in the park."""
    total_snakes = 200
    num_boa_constrictors = 40
    num_pythons = 3 * num_boa_constrictors
    num_rattlesnakes = total_snakes - num_boa_constrictors - num_pythons
    result = num_rattlesnakes
    return result

print(solution())