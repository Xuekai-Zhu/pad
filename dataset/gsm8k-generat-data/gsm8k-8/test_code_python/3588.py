def solution():
    # Define the number of bedbugs on the first day
    initial_bedbugs = x
    
    # Define the growth rate of the bedbugs
    growth_rate = 3

    # Calculate the total number of bedbugs after four days
    total_bedbugs = initial_bedbugs * growth_rate ** 4

    # Solve for the initial number of bedbugs
    initial_bedbugs = 810 / growth_rate ** 4
    result = initial_bedbugs
    return result

print(solution())