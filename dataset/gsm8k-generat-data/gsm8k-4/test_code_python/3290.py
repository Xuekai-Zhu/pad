def solution():
    """Working together, four pugs can clean their house in 45 minutes. In how many minutes will 15 pugs working together be able to clean their house?"""
    # Define the number of pugs and the time it takes for them to clean the house
    pugs = 4
    time = 45

    # Use the formula: pugs * time = constant
    constant = pugs * time

    # Use the constant to calculate the time it will take for 15 pugs to clean the house
    pugs = 15
    time = constant / pugs

    # Return the result
    result = time
    return result

print(solution())