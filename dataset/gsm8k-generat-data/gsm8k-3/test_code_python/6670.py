def solution():
    """Three blue chips are in a jar which is 10% of the entire chips. If 50% of the chips are white and the rest are green, how many green chips are there?"""
    # Define the percentage of blue chips in the jar
    BLUE_PERCENTAGE = 10

    # Define the number of blue chips in the jar
    blue_chips = 3

    # Calculate the total number of chips in the jar
    total_chips = (blue_chips / BLUE_PERCENTAGE) * 100

    # Calculate the number of white chips
    white_chips = total_chips * 0.5

    # Calculate the number of green chips
    green_chips = total_chips - blue_chips - white_chips

    # Display the number of green chips
    result = green_chips
    return result

print(solution())