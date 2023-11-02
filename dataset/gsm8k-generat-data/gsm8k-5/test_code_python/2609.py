def solution():
    beads_per_bracelet = 8  # Each bracelet requires 8 beads
    nancy_beads = 40 + 20  # Nancy has 40 metal beads and 20 more pearl beads
    crystal_beads = 20  # Rose has 20 crystal beads
    stone_beads = 2 * crystal_beads  # Rose has twice as many stone beads as crystal beads
    total_beads = nancy_beads + crystal_beads + stone_beads  # Total number of beads Nancy and Rose have

    # Calculate the total number of bracelets Nancy and Rose can make
    total_bracelets = total_beads // beads_per_bracelet
    result = total_bracelets
    return result

print(solution())