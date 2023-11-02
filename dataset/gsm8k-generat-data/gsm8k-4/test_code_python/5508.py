def solution():
    """Carly is making a beaded corset. She's going to add 50 rows of purple beads with 20 beads per row, 40 rows of blue beads with 18 beads per row, and 80 gold beads. If beads cost $1 per 10 beads, how much do all the beads she bought cost?"""
    # Define the number of beads per row for each color
    PURPLE_BEADS_PER_ROW = 20
    BLUE_BEADS_PER_ROW = 18

    # Calculate the total number of purple beads and blue beads
    purple_beads = 50 * PURPLE_BEADS_PER_ROW
    blue_beads = 40 * BLUE_BEADS_PER_ROW

    # Calculate the total number of beads
    total_beads = purple_beads + blue_beads + 80

    # Calculate the total cost of the beads
    bead_cost = (total_beads // 10) * 1

    # Return the result
    result = bead_cost
    return result

print(solution())