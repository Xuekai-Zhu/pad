def solution():
    """Anna has a certain number of phone chargers and five times more laptop chargers than phone chargers. If she has 24 chargers total, how many phone chargers does she have?"""
    # Define the number of phone chargers as x
    x = None

    # Calculate the number of laptop chargers as 5x
    laptop_chargers = 5 * x

    # Calculate the total number of chargers
    total_chargers = x + laptop_chargers

    # Set the total number of chargers to 24 and solve for x
    x = (24 / 6)
    
    # Return the result
    result = x
    return result

print(solution())