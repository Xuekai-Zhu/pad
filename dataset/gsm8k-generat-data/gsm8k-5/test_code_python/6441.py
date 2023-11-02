def solution():
    num_friends = 8  # Jaco has 8 friends
    cost_per_friend = 9  # Jaco wants to buy gifts worth $9 for each friend
    total_friend_cost = num_friends * cost_per_friend  # Total cost of gifts for all 8 friends
    remaining_budget = 100 - total_friend_cost  # Remaining budget after buying gifts for friends
    mother_father_budget = remaining_budget / 2  # Equal budget for mother and father's gifts
    result = mother_father_budget
    return result

print(solution())