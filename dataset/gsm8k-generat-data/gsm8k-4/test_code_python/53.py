def solution():
    """Caleb bought 10 cartons of ice cream and 4 cartons of frozen yoghurt. Each carton of ice cream cost $4 and each carton of frozen yoghurt cost $1. How much more did Caleb spend on ice cream than on frozen yoghurt?"""
    # Define the prices and quantities of ice cream and frozen yoghurt
    ice_cream_price = 4
    frozen_yoghurt_price = 1
    ice_cream_quantity = 10
    frozen_yoghurt_quantity = 4

    # Calculate the total amount spent on ice cream and frozen yoghurt
    ice_cream_total = ice_cream_price * ice_cream_quantity
    frozen_yoghurt_total = frozen_yoghurt_price * frozen_yoghurt_quantity

    # Calculate the difference in cost between ice cream and frozen yoghurt
    cost_difference = ice_cream_total - frozen_yoghurt_total

    # return the result
    result = cost_difference
    return result

print(solution())