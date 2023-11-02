def solution():
    """A store is having an anniversary sale. A tub of ice cream costs $2 less than its original price of $12 and the juice is sold at $2 for 5 cans. How much will you pay if you buy two tubs of ice cream and 10 cans of juice?"""
    ice_cream_price = 12 - 2
    juice_price = 2/5
    total_ice_cream_cost = 2 * ice_cream_price
    total_juice_cost = 10/5 * 2 * juice_price
    total_cost = total_ice_cream_cost + total_juice_cost
    result = total_cost
    return result

print(solution())