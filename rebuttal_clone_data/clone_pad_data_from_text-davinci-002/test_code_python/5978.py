def solution():
    beads_per_bracelet = 12
    total_beads = 528
    large_beads = beads_per_bracelet / 2
    small_beads = large_beads
    total_beads = large_beads + small_beads
    bracelets = total_beads / beads_per_bracelet
    result = bracelets
    return result

print(solution())