def solution():
    """Cally and Danny washed their clothes. Cally has 10 white shirts, 5 colored shirts, 7 pairs of shorts, and 6 pairs of pants, while Danny has 6 white shirts, 8 colored shirts, 10 shorts, and 6 pairs of pants. How many clothes did they wash?"""
    # Calculate the total number of clothes Cally washed
    cally_white_shirts = 10
    cally_colored_shirts = 5
    cally_shorts = 7
    cally_pants = 6
    cally_total = cally_white_shirts + cally_colored_shirts + cally_shorts + cally_pants

    # Calculate the total number of clothes Danny washed
    danny_white_shirts = 6
    danny_colored_shirts = 8
    danny_shorts = 10
    danny_pants = 6
    danny_total = danny_white_shirts + danny_colored_shirts + danny_shorts + danny_pants

    # Calculate the total number of clothes washed
    total = cally_total + danny_total

    # Display the total number of clothes washed
    result = total
    return result

print(solution())