def solution():
    """Nancy and Rose are making bracelets, and there are eight beads in each bracelet. Nancy has 40 metal beads and 20 more pearl beads. Rose has 20 crystal beads and twice as many stone beads as crystal beads. How many bracelets can Nancy and Rose make?"""
    # Define the number of beads per bracelet
    beads_per_bracelet = 8

    # Define Nancy's beads
    nancy_metal_beads = 40
    nancy_pearl_beads = nancy_metal_beads + 20

    # Define Rose's beads
    rose_crystal_beads = 20
    rose_stone_beads = 2 * rose_crystal_beads

    # Calculate the total number of beads
    total_beads = nancy_metal_beads + nancy_pearl_beads + rose_crystal_beads + rose_stone_beads

    # Calculate the total number of bracelets
    total_bracelets = total_beads // beads_per_bracelet

    result = total_bracelets
    return result

print(solution())