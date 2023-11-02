def solution():
    Nancy_metal = 40
    Nancy_pearl = 20
    Rose_crystal = 20
    Rose_stone = 2 * Rose_crystal
    total_beads = Nancy_metal + Nancy_pearl + Rose_crystal + Rose_stone
    beads_per_bracelet = 8
    bracelets = total_beads / beads_per_bracelet
    result = bracelets
    return result

print(solution())