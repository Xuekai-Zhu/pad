def solution():
    # Define the number of beads each person has
    nancy_metal_beads = 40
    nancy_pearl_beads = nancy_metal_beads + 20
    rose_crystal_beads = 20
    rose_stone_beads = 2 * rose_crystal_beads

    # Calculate the number of bracelets each person can make
    nancy_bracelets = (nancy_metal_beads + nancy_pearl_beads) // 8
    rose_bracelets = (rose_crystal_beads + rose_stone_beads) // 8

    # Calculate the total number of bracelets they can make together
    total_bracelets = nancy_bracelets + rose_bracelets
    result = total_bracelets
    return result

print(solution())