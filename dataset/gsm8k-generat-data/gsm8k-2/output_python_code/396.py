def solution():
    """Ten friends decide to get an end-of-year gift for their teacher. They plan to split the cost of the gift equally. But four of the group drop out. The remaining friends split the cost equally among themselves. If each share is now $8 more, how much does the gift cost, in dollars?"""
    initial_friends = 10
    remaining_friends = initial_friends - 4
    initial_cost = 8 * remaining_friends
    final_cost = initial_cost + 8 * remaining_friends
    result = final_cost
    return result

print(solution())