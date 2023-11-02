def solution():
    # Calculate the number of amber beads
    amber_beads = 2 * 7  # twice as many amber beads as amethyst
    # Calculate the total number of amethyst and amber beads
    total_aa_beads = 7 + amber_beads
    # Calculate the number of turquoise beads
    turquoise_beads = 40 - total_aa_beads  # total number of beads minus the number of amethyst and amber beads
    result = turquoise_beads
    return result

print(solution())