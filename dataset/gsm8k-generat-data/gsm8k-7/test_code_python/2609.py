def solution():
    nancy_metal_beads = 40
    nancy_pearl_beads = 20
    rose_crystal_beads = 20
    rose_stone_beads = 2 * rose_crystal_beads

    # Calculate the total number of beads Nancy has
    total_nancy_beads = nancy_metal_beads + nancy_pearl_beads

    # Calculate the total number of beads Rose has
    total_rose_beads = rose_crystal_beads + rose_stone_beads

    # Calculate the total number of bracelets Nancy and Rose can make
    total_bracelets = (total_nancy_beads + total_rose_beads) // 8
    result = total_bracelets
    return result

print(solution())