def solution():
    num_friends = 10
    num_dropped_out = 4
    cost_per_share_increase = 8

    # Calculate the number of friends who will split the cost
    num_remaining_friends = num_friends - num_dropped_out

    # Calculate the original cost per share
    original_cost_per_share = total_cost / num_friends

    # Calculate the new cost per share
    new_cost_per_share = original_cost_per_share + cost_per_share_increase

    # Calculate the total cost of the gift
    total_cost = new_cost_per_share * num_remaining_friends
    result = total_cost
    return result

print(solution())