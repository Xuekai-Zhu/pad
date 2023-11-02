def solution():
    """Michelle uses 40 beads in making a necklace. She uses 5 blue beads and 2 times as many red beads as blue beads. Then she uses the same number of white beads as the blue and red beads combined. If the rest of the beads she uses are silver, how many silver beads does she use?"""
    # Define the number of blue beads
    blue_beads = 5

    # Calculate the number of red beads
    red_beads = 2 * blue_beads

    # Calculate the total number of blue and red beads
    blue_red_beads = blue_beads + red_beads

    # Calculate the number of white beads
    white_beads = blue_red_beads

    # Calculate the total number of colored beads
    colored_beads = blue_beads + red_beads + white_beads

    # Calculate the number of silver beads
    silver_beads = 40 - colored_beads

    # Display the number of silver beads
    result = silver_beads
    return result

print(solution())