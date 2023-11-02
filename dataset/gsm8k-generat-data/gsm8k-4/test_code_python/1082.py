def solution():
    """Alfred is storing a tonne of maize each month for the next 2 years. If 5 tonnes are stolen and 8 tonnes are given to him as a donation, how many tonnes of maize does he have at the end of the 2 years."""
    
    # Define the total number of months in 2 years
    TOTAL_MONTHS = 24

    # Calculate the total amount of maize stored in 2 years
    total_maize = TOTAL_MONTHS

    # Subtract the stolen and donated maize
    total_maize -= 5
    total_maize += 8

    # return the result
    result = total_maize
    return result

print(solution())