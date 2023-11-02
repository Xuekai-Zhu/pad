def solution():
    
    beads_per_bracelet = 8
    total_beads_needed = beads_per_bracelet * 6
    beads_available = 36
    beads_needed = total_beads_needed - beads_available
    result = beads_needed
    return result

print(solution())