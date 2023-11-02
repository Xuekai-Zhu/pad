def solution():
    
    metal_beads = 40
    pearl_beads = metal_beads + 20
    crystal_beads = 20
    stone_beads = 2 * crystal_beads
    total_beads = metal_beads + pearl_beads + crystal_beads + stone_beads
    bracelets = total_beads // 8
    result = bracelets
    return result

print(solution())