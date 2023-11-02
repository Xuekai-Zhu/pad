def solution():
    """Jaco wants to buy Christmas gifts for his 8 friends that are worth $9 each. Also, he wants to buy gifts for his mother and father that are of the same amount. He has a $100 budget to buy all gifts. How much is Jaco's budget for each of his mother and father's gift?"""
    num_friends = 8
    friend_gift_price = 9
    friends_total_cost = num_friends * friend_gift_price
    mother_father_budget = (100 - friends_total_cost) / 2
    result = mother_father_budget
    return result

print(solution())