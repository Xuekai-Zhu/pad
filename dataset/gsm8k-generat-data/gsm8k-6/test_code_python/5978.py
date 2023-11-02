def solution():
    # Calculate the number of small beads Caitlin has
    total_beads = 528
    large_beads = 12
    small_beads = total_beads / 2 - large_beads

    # Calculate how many bracelets can be made
    beads_per_bracelet = large_beads + 2 * small_beads
    bracelets = total_beads / beads_per_bracelet

    result = bracelets
    return result

print(solution())