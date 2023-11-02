def solution():
    num_cartons_ice_cream = 10
    cost_per_carton_ice_cream = 4

    num_cartons_frozen_yogurt = 4
    cost_per_carton_frozen_yogurt = 1

    # Calculate the total cost of all cartons of ice cream
    total_cost_ice_cream = num_cartons_ice_cream * cost_per_carton_ice_cream

    # Calculate the total cost of all cartons of frozen yogurt
    total_cost_frozen_yogurt = num_cartons_frozen_yogurt * cost_per_carton_frozen_yogurt

    # Calculate the difference in cost between ice cream and frozen yogurt
    difference_in_cost = total_cost_ice_cream - total_cost_frozen_yogurt
    result = difference_in_cost
    return result

print(solution())