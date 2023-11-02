def solution():
    """If olivine has 5 more precious stones than agate and diamond has 11 more precious stones than olivine, how many precious stones do they have together if agate has 30 precious stones?"""
    # Define the number of precious stones of agate
    agate_precious_stones = 30

    # Calculate the number of precious stones of olivine
    olivine_precious_stones = agate_precious_stones + 5

    # Calculate the number of precious stones of diamond
    diamond_precious_stones = olivine_precious_stones + 11

    # Calculate the total number of precious stones
    total_precious_stones = agate_precious_stones + olivine_precious_stones + diamond_precious_stones

    # Return the result
    result = total_precious_stones
    return result

print(solution())