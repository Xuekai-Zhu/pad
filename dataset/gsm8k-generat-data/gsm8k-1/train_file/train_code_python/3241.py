def solution():
    """Jane purchased 15 ice cream cones and 5 cups of pudding. Each ice cream cone cost $5 and each cup of pudding cost $2. How much more did Jane spend on ice cream than on pudding, in dollars?"""
    ice_cream_cost = 5
    pudding_cost = 2
    ice_cream_quantity = 15
    pudding_quantity = 5
    total_ice_cream_cost = ice_cream_cost * ice_cream_quantity
    total_pudding_cost = pudding_cost * pudding_quantity
    difference = total_ice_cream_cost - total_pudding_cost
    result = difference
    return result

print(solution())