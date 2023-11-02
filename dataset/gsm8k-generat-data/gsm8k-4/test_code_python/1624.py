def solution():
    """A kilogram of pork costs $6 while a kilogram of chicken costs $2 less. How much will a 3-kilogram of chicken and a kilogram of pork cost?"""
    # Define the cost of pork per kilogram
    pork_cost = 6

    # Define the cost of chicken as $2 less than pork
    chicken_cost = pork_cost - 2

    # Calculate the cost of 3 kilograms of chicken and 1 kilogram of pork
    total_cost = (3 * chicken_cost) + pork_cost

    # Return the result
    result = total_cost
    return result

print(solution())