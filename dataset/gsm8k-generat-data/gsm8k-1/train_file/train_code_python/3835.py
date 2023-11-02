def solution():
    """Five shirts together cost $85. Of the 5 shirts, there are 3 shirts that cost $15 each. If the remaining shirts are each equal in value, what is the cost, in dollars, of one of the remaining shirts?"""
    total_cost = 85
    price_of_three_shirts = 3 * 15
    cost_of_two_shirts = total_cost - price_of_three_shirts
    cost_of_one_shirt = cost_of_two_shirts / 2
    result = cost_of_one_shirt
    return result

print(solution())