def solution():
    """A store is having an anniversary sale. A tub of ice cream costs $2 less than its original price of $12 and the juice is sold at $2 for 5 cans. How much will you pay if you buy two tubs of ice cream and 10 cans of juice?"""
    original_ice_cream_price = 12
    ice_cream_discount = 2
    ice_cream_price = original_ice_cream_price - ice_cream_discount
    ice_cream_quantity = 2
    juice_quantity = 10
    juice_price = 2/5
    total_ice_cream_price = ice_cream_quantity * ice_cream_price
    total_juice_price = juice_quantity * juice_price
    total_price = total_ice_cream_price + total_juice_price
    result = total_price
    return result

print(solution())