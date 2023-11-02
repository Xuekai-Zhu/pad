def solution():
    # Calculate the total number of beads bought by each sister
    elizabeth_beads = 1 + 2  # Elizabeth bought 1 pack of red, 2 packs of clear beads
    margareth_beads = 3 + 4  # Margareth bought 3 packs of blue, 4 packs of red beads
    total_beads = elizabeth_beads + margareth_beads  # Total number of beads
    beads_per_sister = 20  # Each pack of beads contains 20 pieces of beads

    # Calculate the difference in beads between the two sisters
    difference = total_beads - beads_per_sister
    result = difference
    return result

print(solution())