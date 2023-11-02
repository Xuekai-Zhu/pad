def solution():
    large_beads_per_bracelet = 12  # Each bracelet uses 12 large beads
    small_beads_per_bracelet = 2 * large_beads_per_bracelet  # Each bracelet uses twice as many small beads
    total_beads = 528  # Caitlin has 528 beads in total, with equal amounts of large and small beads

    # Calculate the number of bracelets Caitlin can make
    num_bracelets = total_beads // (large_beads_per_bracelet + small_beads_per_bracelet)
    result = num_bracelets
    return result

print(solution())