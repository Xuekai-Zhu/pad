def solution():
    # Calculate the total cost
    total_cost = 10 + (5 * 5) + (4 * 2.5) + (5 * 2)

    # Divide the total cost by the number of friends
    num_friends = 5
    cost_per_friend = total_cost / num_friends

    result = cost_per_friend
    return result

print(solution())