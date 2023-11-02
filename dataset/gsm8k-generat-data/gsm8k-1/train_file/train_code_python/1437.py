def solution():
    """ Bobby made a big batch of soup weighing 80 kg. Each day the batch gets reduced by half. How many kg will it reach on the fourth day after he made the soup?"""
    initial_weight = 80
    days_passed = 4
    final_weight = initial_weight / (2**days_passed)
    result = final_weight
    return result

print(solution())