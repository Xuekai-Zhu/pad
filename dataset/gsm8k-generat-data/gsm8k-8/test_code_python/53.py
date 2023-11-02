def solution():
    # Define the number of cartons of ice cream and frozen yogurt
    ice_cream_cartons = 10
    frozen_yogurt_cartons = 4

    # Define the cost of each carton
    ice_cream_cost = 4
    frozen_yogurt_cost = 1

    # Calculate the total cost of the ice cream and frozen yogurt
    ice_cream_total_cost = ice_cream_cartons * ice_cream_cost
    frozen_yogurt_total_cost = frozen_yogurt_cartons * frozen_yogurt_cost

    # Calculate the difference in cost between ice cream and frozen yogurt
    difference_cost = ice_cream_total_cost - frozen_yogurt_total_cost
    result = difference_cost
    return result

print(solution())