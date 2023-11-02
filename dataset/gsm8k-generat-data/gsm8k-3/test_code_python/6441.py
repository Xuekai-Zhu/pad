def solution():
    """Jaco wants to buy Christmas gifts for his 8 friends that are worth $9 each.  Also, he wants to buy gifts for his mother and father that are of the same amount. He has a $100 budget to buy all gifts. How much is Jaco's budget for each of his mother and father's gift?"""
    # Define the cost per gift for friends
    FRIEND_GIFT_COST = 9

    # Define the number of friends
    num_friends = 8

    # Calculate the total cost of gifts for friends
    friend_gift_cost = num_friends * FRIEND_GIFT_COST

    # Calculate the remaining budget for gifts for Jaco's parents
    parent_budget = 100 - friend_gift_cost

    # Divide the remaining budget equally between Jaco's mother and father
    parent_gift_cost = parent_budget / 2

    # Display the budget for each of Jaco's parents' gifts
    result = parent_gift_cost
    return result

print(solution())