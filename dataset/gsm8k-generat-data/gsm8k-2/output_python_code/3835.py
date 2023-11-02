def solution():
    """Five shirts together cost $85. Of the 5 shirts, there are 3 shirts that cost $15 each. If the remaining shirts are each equal in value, what is the cost, in dollars, of one of the remaining shirts?"""
    total_cost = 85
    cost_of_three_shirts = 3 * 15
    cost_of_two_remaining_shirts = total_cost - cost_of_three_shirts
    cost_of_one_remaining_shirt = cost_of_two_remaining_shirts / 2
    result = cost_of_one_remaining_shirt
    return result

print(solution())