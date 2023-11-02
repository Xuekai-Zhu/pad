def solution():
    num_ice_cream_cones = 15
    ice_cream_cone_price = 5

    num_pudding_cups = 5
    pudding_cup_price = 2

    # Calculate the total cost of all ice cream cones
    total_ice_cream_cost = num_ice_cream_cones * ice_cream_cone_price

    # Calculate the total cost of all pudding cups
    total_pudding_cost = num_pudding_cups * pudding_cup_price

    # Calculate the difference in cost between ice cream and pudding
    difference = total_ice_cream_cost - total_pudding_cost
    result = difference
    return result

print(solution())