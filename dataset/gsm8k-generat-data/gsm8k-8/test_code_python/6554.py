def solution():
    # Define the number of blue and red beads
    blue_beads = 5
    red_beads = 2 * blue_beads

    # Calculate the total number of blue and red beads
    total_beads = blue_beads + red_beads

    # Calculate the number of white beads
    white_beads = total_beads

    # Calculate the total number of beads used
    total_used = blue_beads + red_beads + white_beads

    # Calculate the number of silver beads
    silver_beads = 40 - total_used
    result = silver_beads
    return result

print(solution())