def solution():
    """Roy has 2 blue pens. He has twice as many black and 2 less than twice as many red than black pens. How many pens does Roy have in all?"""
    # Define the number of blue pens
    blue_pens = 2

    # Calculate the number of black pens
    black_pens = 2 * blue_pens

    # Calculate the number of red pens
    red_pens = 2 * black_pens - 2

    # Calculate the total number of pens
    total_pens = blue_pens + black_pens + red_pens

    # Display the total number of pens
    result = total_pens
    return result

print(solution())