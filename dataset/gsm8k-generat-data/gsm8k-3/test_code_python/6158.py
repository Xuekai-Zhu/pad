def solution():
    """Joseph has a refrigerator, a water heater in his house, and an electric oven that consumes power at different rates. The total amount of money that Joseph pays for the energy used by the refrigerator is three times the amount he pays for the power used by the water heater. If the electric oven uses power worth $500 in a month, twice what Joseph pays for the power the water heater uses, calculate the total amount he pays for the power used by these gadgets."""
    
    # Let x be the amount Joseph pays for the power the water heater uses
    # Then the amount he pays for the refrigerator is 3x
    # The electric oven uses power worth $500, which is twice what Joseph pays for the water heater, so he pays $500/2 = $250 for the water heater
    x = 250
    
    # Calculate the amount Joseph pays for the refrigerator
    refrigerator_cost = 3*x
    
    # Calculate the total amount Joseph pays for the power used by all gadgets
    total_cost = refrigerator_cost + x + 500
    
    result = total_cost
    return result

print(solution())