def solution():
    """36 liters of diesel fuel is worth €18. The tank of this pickup truck can hold 64 liters. How much does a full tank of diesel fuel cost?"""
    # Calculate the cost of 1 liter of diesel fuel
    cost_per_liter = 18 / 36

    # Calculate the cost of a full tank of diesel fuel
    full_tank_cost = cost_per_liter * 64

    # Display the cost of a full tank of diesel fuel
    result = full_tank_cost
    return result

print(solution())