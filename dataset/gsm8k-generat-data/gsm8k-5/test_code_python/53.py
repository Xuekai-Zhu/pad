def solution():
    ice_cream_cartons = 10
    frozen_yoghurt_cartons = 4
    ice_cream_cost = 4  # $4 per carton of ice cream
    frozen_yoghurt_cost = 1  # $1 per carton of frozen yoghurt

    # Calculate the total cost of ice cream and frozen yoghurt
    total_cost_ice_cream = ice_cream_cartons * ice_cream_cost
    total_cost_frozen_yoghurt = frozen_yoghurt_cartons * frozen_yoghurt_cost

    # Calculate the difference in cost between ice cream and frozen yoghurt
    cost_difference = total_cost_ice_cream - total_cost_frozen_yoghurt
    result = cost_difference
    return result

print(solution())