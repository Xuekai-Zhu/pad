def solution():
    """If Olivine has 5 more precious stones than agate and diamond has 11 more precious stones than Olivine, how many precious stones do they have together if agate has 30 precious stones?"""
    # Define the number of precious stones Agate has
    agate = 30

    # Calculate the number of precious stones Olivine has
    olivine = agate + 5

    # Calculate the number of precious stones Diamond has
    diamond = olivine + 11

    # Calculate the total number of precious stones
    total = agate + olivine + diamond

    # Display the total number of precious stones
    result = total
    return result

print(solution())