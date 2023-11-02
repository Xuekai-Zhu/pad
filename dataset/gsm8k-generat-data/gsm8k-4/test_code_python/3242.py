def solution():
    """Jane purchased 15 ice cream cones and 5 cups of pudding. Each ice cream cone cost $5 and each cup of pudding cost $2. How much more did Jane spend on ice cream than on pudding, in dollars?"""
    # Define the cost of one ice cream cone and one cup of pudding
    ICE_CREAM_COST = 5
    PUDDING_COST = 2

    # Define the number of ice cream cones and cups of pudding purchased
    ICE_CREAM_CONES = 15
    PUDDING_CUPS = 5

    # Calculate the total cost of ice cream and pudding purchased
    ice_cream_total = ICE_CREAM_COST * ICE_CREAM_CONES
    pudding_total = PUDDING_COST * PUDDING_CUPS

    # Calculate the difference in cost
    cost_difference = ice_cream_total - pudding_total

    # return the result
    result = cost_difference
    return result

print(solution())