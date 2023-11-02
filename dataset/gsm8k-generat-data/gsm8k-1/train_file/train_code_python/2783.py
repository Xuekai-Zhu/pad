def solution():
    """Rubble has $15 in his pocket and he needs to buy 2 notebooks and 2 pens. Each notebook cost $4.00 meanwhile each pen cost $1.50. How much money will be left from Rubble after the purchase?"""
    money_in_pocket = 15
    notebooks_cost = 4 * 2
    pens_cost = 1.5 * 2
    total_cost = notebooks_cost + pens_cost
    money_left = money_in_pocket - total_cost
    result = money_left
    return result

print(solution())