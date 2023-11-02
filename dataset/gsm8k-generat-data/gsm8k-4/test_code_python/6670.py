def solution():
    """Three blue chips are in a jar which is 10% of the entire chips. If 50% of the chips are white and the rest are green, how many green chips are there?"""
    # Define the proportion of blue chips in the jar
    blue_proportion = 0.1

    # Calculate the total number of chips in the jar (assuming 100%)
    total_chips = 3 / blue_proportion

    # Calculate the number of white chips in the jar
    white_chips = total_chips * 0.5

    # Calculate the number of green chips in the jar
    green_chips = total_chips - 3 - white_chips

    # return the result
    result = green_chips
    return result

print(solution())