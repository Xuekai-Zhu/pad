def solution():
    """Alfred is storing a tonne of maize each month for the next 2 years.  If 5 tonnes are stolen and 8 tonnes are given to him as a donation, how many tonnes of maize does he have at the end of the 2 years."""
    # Define the number of months in 2 years
    MONTHS = 24

    # Calculate the total number of tonnes of maize stored over the 2 years
    total_maize = MONTHS

    # Subtract the stolen maize and add the donated maize
    total_maize = total_maize - 5 + 8

    # Display the total number of tonnes of maize
    result = total_maize
    return result

print(solution())