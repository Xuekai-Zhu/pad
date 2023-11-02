def solution():
    """Ten friends decide to get an end-of-year gift for their teacher. They plan to split the cost of the gift equally. But four of the group drop out. The remaining friends split the cost equally among themselves. If each share is now $8 more, how much does the gift cost, in dollars?"""
    initial_cost_per_person = 0
    final_cost_per_person = initial_cost_per_person + 8
    num_friends_initial = 10
    num_friends_final = num_friends_initial - 4
    total_cost = final_cost_per_person * num_friends_final
    result = total_cost
    return result

print(solution())