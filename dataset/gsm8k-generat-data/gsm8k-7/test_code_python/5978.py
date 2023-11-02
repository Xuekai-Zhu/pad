def solution():
    num_large_beads_per_bracelet = 12
    total_beads = 528

    # Calculate the number of small beads in each bracelet
    num_small_beads_per_bracelet = 2 * num_large_beads_per_bracelet

    # Calculate the total number of bracelets that Caitlin can make
    num_bracelets = total_beads / (num_large_beads_per_bracelet + num_small_beads_per_bracelet)
    result = num_bracelets
    return result

print(solution())