def solution():
    """Bella is making bracelets for her 6 friends. She needs 8 beads per bracelet. She has 36 beads. How many more beads does she need to make all six bracelets?"""
    # Define the number of beads needed per bracelet and the total number of bracelets to make
    BEADS_PER_BRACELET = 8
    BRACELETS_TO_MAKE = 6

    # Define the number of beads Bella has
    beads_owned = 36

    # Calculate the total number of beads needed to make all the bracelets
    total_beads_needed = BEADS_PER_BRACELET * BRACELETS_TO_MAKE

    # Calculate the number of beads needed to make the remaining bracelets
    beads_needed = total_beads_needed - beads_owned

    # Display the number of beads needed
    result = beads_needed
    return result

print(solution())