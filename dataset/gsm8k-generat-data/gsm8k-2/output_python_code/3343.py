def solution():
    """A jar on the family's counter contains change they've been saving for a trip to the ice cream shop. There are 123 pennies, 85 nickels, 35 dimes, and a number of quarters. All five family members get a double scoop, which costs $3 each. After the trip, they have 48 cents left over. How many quarters were in the jar?"""
    # In dollars
    total_cost = 3 * 5
    total_change = (123 * 0.01) + (85 * 0.05) + (35 * 0.1)
    remaining_change = 0.48
    
    # We can set up an equation to solve for the number of quarters:
    # total_change - (number of quarters * 0.25) = total_cost + remaining_change
    num_quarters = int(((total_change - total_cost - remaining_change) / 0.25))

    result = num_quarters
    return result

print(solution())