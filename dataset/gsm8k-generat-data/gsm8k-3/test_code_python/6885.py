def solution():
    """Farrah ordered 4 boxes from Amazon containing 20 matchboxes each. If each matchbox has 300 sticks, calculate the total number of match sticks that Farah ordered?"""
    # Define the number of matchboxes per box and the number of sticks per matchbox
    MATCHBOXES_PER_BOX = 20
    STICKS_PER_MATCHBOX = 300

    # Calculate the total number of matchsticks
    total_sticks = MATCHBOXES_PER_BOX * STICKS_PER_MATCHBOX * 4

    # Display the total number of matchsticks
    result = total_sticks
    return result

print(solution())