def solution():
    """A kilogram of pork costs $6 while a kilogram of chicken costs $2 less. How much will a 3-kilogram of chicken and a kilogram of pork cost?"""
    
    # Define the cost of one kilogram of pork and chicken
    PORK_COST = 6
    CHICKEN_COST = PORK_COST - 2
    
    # Calculate the total cost of 3 kilograms of chicken and 1 kilogram of pork
    total_cost = (3 * CHICKEN_COST) + PORK_COST

    # Display the total cost
    result = total_cost
    return result

print(solution())