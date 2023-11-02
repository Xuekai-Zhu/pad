def solution():
     ice_cream_cones = 15
     pudding_cups = 5
     price_per_cone = 5
     price_per_cup = 2
     total_cone_cost = ice_cream_cones * price_per_cone
     total_cup_cost = pudding_cups * price_per_cup
     difference = total_cone_cost - total_cup_cost
     result = difference
     return result

print(solution())