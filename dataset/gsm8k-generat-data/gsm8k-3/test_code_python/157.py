def solution():
    """A young girl pours 23 blue beads and 16 yellow beads into a bowl. She divides the total into 3 equal parts, removes some beads from each part, and doubles the rest to have 6 beads in each part now. How many beads were removed from each part?"""
    # Define the initial number of blue and yellow beads
    initial_blue_beads = 23
    initial_yellow_beads = 16

    # Calculate the total number of beads
    total_beads = initial_blue_beads + initial_yellow_beads

    # Calculate the number of beads in each of the 3 equal parts
    equal_parts = total_beads // 3

    # Remove some beads from each part
    removed_beads_per_part = equal_parts - 6

    # Return the number of beads removed from each part
    result = removed_beads_per_part
    return result

print(solution())