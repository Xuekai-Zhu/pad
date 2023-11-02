def solution():
    # Determine the number of American swallows and European swallows in the flock
    american_swallows = 2/3 * 90
    european_swallows = 1/3 * 90

    # Calculate the maximum weight each type of swallow can carry
    american_max_weight = 5
    european_max_weight = 2 * american_max_weight

    # Calculate the total weight the flock can carry
    total_max_weight = (american_swallows * american_max_weight) + (european_swallows * european_max_weight)
    result = total_max_weight
    return result

print(solution())