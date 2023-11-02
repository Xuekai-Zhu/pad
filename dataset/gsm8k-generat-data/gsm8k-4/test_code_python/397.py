def solution():
    """Ten friends decide to get an end-of-year gift for their teacher. They plan to split the cost of the gift equally. But four of the group drop out. The remaining friends split the cost equally among themselves. If each share is now $8 more, how much does the gift cost, in dollars?"""
    # Define the initial number of friends and the initial cost per friend
    initial_friends = 10
    initial_cost_per_friend = None

    # Define the remaining number of friends, and the increased cost per friend
    remaining_friends = 6
    increased_cost_per_friend = "$8"

    # Calculate the initial cost of the gift
    initial_gift_cost = initial_friends * initial_cost_per_friend

    # Calculate the final cost of the gift
    final_gift_cost = remaining_friends * (initial_cost_per_friend + increased_cost_per_friend)

    # return the result
    result = final_gift_cost
    return result

print(solution())