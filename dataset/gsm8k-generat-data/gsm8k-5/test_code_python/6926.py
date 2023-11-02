def solution():
    amethyst_beads = 7  # There are 7 amethyst beads
    amber_beads = 2 * amethyst_beads  # There are twice as many amber beads as amethysts
    total_beads = 40  # The necklace has a total of 40 beads

    # Calculate the number of turquoise beads
    turquoise_beads = total_beads - amethyst_beads - amber_beads
    result = turquoise_beads
    return result

print(solution())