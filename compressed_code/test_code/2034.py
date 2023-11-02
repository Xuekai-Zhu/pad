def solution():
    
    nancy_metal_beads = 40
    nancy_pearl_beads = nancy_metal_beads + 20
    rose_crystal_beads = 20
    rose_stone_beads = 2 * rose_crystal_beads
    total_beads = nancy_metal_beads + nancy_pearl_beads + rose_crystal_beads + rose_stone_beads
    bracelets = total_beads // 8
    result = bracelets
    return result

print(solution())