def solution():
    # Find the number of American and European swallows in the flock
    american_swallows = 2/3 * 90  # twice as many American as European swallows
    european_swallows = 1/3 * 90
    # Find the maximum weight the flock can carry
    total_weight = 5 * american_swallows + 2 * 5 * european_swallows  # European swallow can carry twice the weight as the American swallow
    result = total_weight
    return result

print(solution())