def solution():
    total_cost = 21
    num_spoons_in_set = 7
    num_spoons_to_buy = 5

    # Calculate the cost per spoon in the set
    cost_per_spoon = total_cost / num_spoons_in_set

    # Calculate the cost of buying 5 spoons separately
    cost_of_5_spoons = cost_per_spoon * num_spoons_to_buy
    result = cost_of_5_spoons
    return result

print(solution())