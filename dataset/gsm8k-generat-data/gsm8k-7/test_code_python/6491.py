def solution():
    num_channels = 200
    first_100_cost = 100
    next_100_cost = 50

    # Calculate the total cost of the first 100 channels
    total_first_100_cost = first_100_cost

    # Calculate the total cost of the next 100 channels
    total_next_100_cost = (num_channels - 100) * next_100_cost

    # Calculate the total cost of all channels
    total_cost = total_first_100_cost + total_next_100_cost

    # Split the cost evenly with the roommate
    split_cost = total_cost / 2
    result = split_cost
    return result

print(solution())