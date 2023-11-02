def solution():
    """Working together, four pugs can clean their house in 45 minutes. In how many minutes will 15 pugs working together be able to clean their house?"""
    # Define the initial variables
    pugs1 = 4
    time1 = 45

    # Calculate the variable for the second equation
    pugs2 = 15
    time2 = (pugs1 * time1) / pugs2

    # Display the time it would take for 15 pugs to clean the house
    result = time2
    return result

print(solution())