def solution():
    """Caleb bought 10 cartons of ice cream and 4 cartons of frozen yoghurt. Each carton of ice cream cost $4 and each carton of frozen yoghurt cost $1. How much more did Caleb spend on ice cream than on frozen yoghurt?"""
    # Define the number of cartons of ice cream and frozen yoghurt
    ice_cream_cartons = 10
    yogurt_cartons = 4

    # Calculate the total cost of the ice cream and frozen yoghurt
    ice_cream_cost = ice_cream_cartons * 4
    yogurt_cost = yogurt_cartons * 1

    # Calculate the difference in cost between ice cream and frozen yoghurt
    cost_difference = ice_cream_cost - yogurt_cost

    # Return the result
    result = cost_difference
    return result

print(solution())