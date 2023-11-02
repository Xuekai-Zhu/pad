def solution():
    """Cally and Danny washed their clothes. Cally has 10 white shirts, 5 colored shirts, 7 pairs of shorts, and 6 pairs of pants, while Danny has 6 white shirts, 8 colored shirts, 10 shorts, and 6 pairs of pants. How many clothes did they wash?"""
    # Define the number of clothes for each item for Cally
    cally_white = 10
    cally_colored = 5
    cally_shorts = 7
    cally_pants = 6

    # Define the number of clothes for each item for Danny
    danny_white = 6
    danny_colored = 8
    danny_shorts = 10
    danny_pants = 6

    # Calculate the total number of clothes washed
    total_clothes = cally_white + cally_colored + cally_shorts + cally_pants + danny_white + danny_colored + danny_shorts + danny_pants

    # return the result
    result = total_clothes
    return result

print(solution())