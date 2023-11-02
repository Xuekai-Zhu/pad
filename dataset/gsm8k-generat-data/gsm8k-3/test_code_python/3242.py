def solution():
    """Jane purchased 15 ice cream cones and 5 cups of pudding. Each ice cream cone cost $5 and each cup of pudding cost $2. How much more did Jane spend on ice cream than on pudding, in dollars?"""
    # Define the cost of an ice cream cone and a cup of pudding
    ICE_CREAM_COST = 5
    PUDDING_COST = 2

    # Define the number of ice cream cones and cups of pudding purchased by Jane
    ice_cream_cones = 15
    pudding_cups = 5

    # Calculate the total cost of the ice cream cones
    ice_cream_cost = ice_cream_cones * ICE_CREAM_COST

    # Calculate the total cost of the cups of pudding
    pudding_cost = pudding_cups * PUDDING_COST

    # Calculate the difference in cost between the ice cream and pudding
    difference = ice_cream_cost - pudding_cost

    # Display the difference in cost
    result = difference
    return result

print(solution())