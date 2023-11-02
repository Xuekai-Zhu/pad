def solution():
    """Jaco wants to buy Christmas gifts for his 8 friends that are worth $9 each. Also, he wants to buy gifts for his mother and father that are of the same amount. He has a $100 budget to buy all gifts. How much is Jaco's budget for each of his mother and father's gift?"""
    # Define the number of friends and their gift price
    num_friends = 8
    friend_gift_price = 9

    # Calculate the total cost of gifts for friends
    friends_gift_cost = num_friends * friend_gift_price

    # Calculate the remaining budget
    remaining_budget = 100 - friends_gift_cost

    # Calculate the budget for each of Jaco's parents
    parent_gift_budget = remaining_budget / 2

    result = parent_gift_budget
    return result

print(solution())