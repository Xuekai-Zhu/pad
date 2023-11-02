def solution():
    """Jane purchased 15 ice cream cones and 5 cups of pudding. Each ice cream cone cost $5 and each cup of pudding cost $2. How much more did Jane spend on ice cream than on pudding, in dollars?"""
    ice_cream_cone_cost = 5
    pudding_cup_cost = 2
    num_ice_cream_cones = 15
    num_pudding_cups = 5
    total_ice_cream_cost = ice_cream_cone_cost * num_ice_cream_cones
    total_pudding_cost = pudding_cup_cost * num_pudding_cups
    difference = total_ice_cream_cost - total_pudding_cost
    result = difference
    return result

print(solution())