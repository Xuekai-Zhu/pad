def solution():
    """Ten friends decide to get an end-of-year gift for their teacher. They plan to split the cost of the gift equally. But four of the group drop out. The remaining friends split the cost equally among themselves. If each share is now $8 more, how much does the gift cost, in dollars?"""
    # Define the initial number of friends and cost of the gift
    initial_friends = 10
    initial_cost = x
    # where x represents the unknown cost of the gift

    # Calculate the cost per initial friend
    cost_per_friend = initial_cost / initial_friends

    # Determine the number of remaining friends and calculate the new cost per friend
    remaining_friends = initial_friends - 4
    new_cost_per_friend = cost_per_friend + 8

    # Calculate the new total cost of the gift
    new_total_cost = new_cost_per_friend * remaining_friends

    # Display the new total cost
    result = new_total_cost
    return result

print(solution())