def solution():
    """A young girl pours 23 blue beads and 16 yellow beads into a bowl. She divides the total into 3 equal parts, removes some beads from each part, and doubles the rest to have 6 beads in each part now. How many beads were removed from each part?"""
    # Define the total number of beads
    total_beads = 23 + 16

    # Divide the total into 3 equal parts
    equal_parts = total_beads / 3

    # Calculate the number of beads in each part before removal
    before_removal = equal_parts / 2

    # Calculate the number of beads removed from each part
    removed_beads = before_removal - 6

    # Return the result
    result = round(removed_beads)
    return result

print(solution())