def solution():
    
    green_beads = 3
    purple_beads = 5
    red_beads = 2 * green_beads
    beads_per_pattern = green_beads + purple_beads + red_beads
    patterns_per_bracelet = 3
    patterns_per_necklace = 5
    beads_per_bracelet = beads_per_pattern * patterns_per_bracelet
    beads_per_necklace = beads_per_pattern * patterns_per_necklace
    beads_per_10_necklaces = beads_per_necklace * 10
    total_beads = beads_per_bracelet + beads_per_10_necklaces
    result = total_beads
    return result

print(solution())