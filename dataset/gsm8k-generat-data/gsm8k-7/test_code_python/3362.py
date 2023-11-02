def solution():
    american_swallow_max_weight = 5
    european_swallow_max_weight = 2 * american_swallow_max_weight
    num_american_swallows = 2 * num_european_swallows
    total_num_swallows = 90

    # Calculate the number of European swallows in the flock
    num_european_swallows = total_num_swallows / 3

    # Calculate the number of American swallows in the flock
    num_american_swallows = 2 * num_european_swallows

    # Calculate the total maximum weight the flock can carry
    total_max_weight = num_european_swallows * european_swallow_max_weight + num_american_swallows * american_swallow_max_weight
    result = total_max_weight
    return result

print(solution())