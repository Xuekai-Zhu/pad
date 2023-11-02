def solution():
    beads_per_bracelet = 8
    total_beads_needed = beads_per_bracelet * 6
    beads_left = 36
    beads_needed = total_beads_needed - beads_left
    result = beads_needed
    return result

print(solution())