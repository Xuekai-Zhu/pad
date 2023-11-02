def solution():
    """Rubble has $15 in his pocket and he needs to buy 2 notebooks and 2 pens. Each notebook cost $4.00 meanwhile each pen cost $1.50. How much money will be left from Rubble after the purchase?"""
    total_cost = (2*4) + (2*1.5)
    left_money = 15 - total_cost
    result = left_money
    return result

print(solution())