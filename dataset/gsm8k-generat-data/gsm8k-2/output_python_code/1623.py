def solution():
    """A kilogram of pork costs $6 while a kilogram of chicken costs $2 less. How much will a 3-kilogram of chicken and a kilogram of pork cost?"""
    pork_price = 6
    chicken_price = pork_price - 2
    total_cost = (3 * chicken_price) + pork_price
    result = total_cost
    return result

print(solution())