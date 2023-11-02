def solution():
    """Peter needs 80 ounces of soda for his party. He sees that 8 oz cans cost $.5 each. How much does he spend on soda if he buys the exact number of cans he needs?"""
    required_cans = 80/8
    can_cost = 0.5
    total_cost = required_cans * can_cost
    result = total_cost
    return result

print(solution())