def solution():
    """Bella is making bracelets for her 6 friends. She needs 8 beads per bracelet. She has 36 beads. How many more beads does she need to make all six bracelets?"""
    # Define the number of beads required per bracelet and the total number of bracelets
    beads_per_bracelet = 8
    total_bracelets = 6

    # Calculate the total number of beads required
    total_beads = beads_per_bracelet * total_bracelets

    # Calculate the number of additional beads needed
    additional_beads = total_beads - 36

    # return the result
    result = additional_beads
    return result

print(solution())