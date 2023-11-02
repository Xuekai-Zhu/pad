def solution():
    """36 liters of diesel fuel is worth €18. The tank of this pickup truck can hold 64 liters. How much does a full tank of diesel fuel cost?"""
    # Define the cost and amount of fuel per liter
    cost_per_liter = 18 / 36
    liters_per_tank = 64

    # Calculate the cost of a full tank of diesel fuel
    cost_per_tank = cost_per_liter * liters_per_tank

    # return the result
    result = cost_per_tank
    return result

print(solution())