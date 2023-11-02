def solution():
    # Calculate the total cost of the three shirts that cost $15 each
    cost_of_three_shirts = 3 * 15

    # Calculate the cost of the remaining two shirts
    cost_of_remaining_shirts = 85 - cost_of_three_shirts

    # Calculate the cost of one remaining shirt
    cost_of_one_remaining_shirt = cost_of_remaining_shirts / 2
    result = cost_of_one_remaining_shirt
    return result

print(solution())