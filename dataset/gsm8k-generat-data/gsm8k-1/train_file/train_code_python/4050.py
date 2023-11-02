def solution():
    """Five friends eat at Wendy's and ordered the following: a platter of Taco Salad that cost $10, 5 orders of Dave's Single hamburger that cost $5 each, 4 sets of french fries that cost $2.50, and 5 cups of peach lemonade that cost $2 each. How much will each of them pay if they will split the bill equally?"""
    total_cost = 10 + (5 * 5) + (4 * 2.5) + (5 * 2)
    num_friends = 5
    cost_per_friend = total_cost / num_friends
    result = cost_per_friend
    return result

print(solution())