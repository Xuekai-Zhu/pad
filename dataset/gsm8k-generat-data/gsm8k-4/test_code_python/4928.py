def solution():
    """ Every 2 years, the number of swans at Rita's pond doubles. Currently, there are 15 swans in the pond. How many swans will there be in ten years? """
    # Define the initial number of swans and the number of years
    INITIAL_SWANS = 15
    YEARS = 10

    # Calculate the final number of swans
    final_swans = INITIAL_SWANS * (2 ** (YEARS // 2))

    # Display the final number of swans
    result = final_swans
    return result

print(solution())