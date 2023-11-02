def solution():
    """Bobby made a big batch of soup weighing 80 kg. Each day the batch gets reduced by half. How many kg will it reach on the fourth day after he made the soup?"""
    initial_weight = 80
    remaining_weight = initial_weight / (2**4)
    result = remaining_weight
    return result

print(solution())