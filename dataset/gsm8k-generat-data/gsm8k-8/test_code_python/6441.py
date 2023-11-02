def solution():
    # Calculate the total cost of the gifts for his friends
    friends_cost = 8 * 9

    # Calculate the remaining budget for his parents' gifts
    remaining_budget = 100 - friends_cost

    # Divide the remaining budget equally between his parents
    parent_gift_budget = remaining_budget / 2

    result = parent_gift_budget
    return result

print(solution())