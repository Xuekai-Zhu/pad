def solution():
    """There are 60 pieces of chips in Lara's bag. One-sixth of the chips are blue. There are 34 red chips and the rest are green. How many green chips are in Lara's bag?"""
    # Define the total number of chips and the fraction that are blue
    total_chips = 60
    blue_fraction = 1/6

    # Calculate the number of blue chips
    blue_chips = total_chips * blue_fraction

    # Calculate the number of red chips
    red_chips = 34

    # Calculate the number of green chips
    green_chips = total_chips - blue_chips - red_chips

    # Display the number of green chips
    result = green_chips
    return result

print(solution())