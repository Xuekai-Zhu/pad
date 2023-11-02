def solution():
     pattern_repeats_bracelet = 3
     pattern_repeats_necklace = 5
     beads_needed_bracelet = pattern_repeats_bracelet * (3 + 5 + (2 * 3))
     beads_needed_necklace = pattern_repeats_necklace * (3 + 5 + (2 * 3))
     total_beads_needed = beads_needed_bracelet + (10 * beads_needed_necklace)
     result = total_beads_needed
     return result

print(solution())