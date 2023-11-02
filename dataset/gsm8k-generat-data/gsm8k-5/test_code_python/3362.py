def solution():
    american_swallow_max_weight = 5  # The American swallow can carry a maximum of 5 pounds
    european_swallow_max_weight = 2 * american_swallow_max_weight  # The European swallow can carry twice the weight of the American swallow
    num_american_swallow = 2/3 * 90  # There are twice as many American swallows as European swallows in the flock
    num_european_swallow = 1/3 * 90
    total_weight = num_american_swallow * american_swallow_max_weight + num_european_swallow * european_swallow_max_weight
    result = total_weight
    return result

print(solution())