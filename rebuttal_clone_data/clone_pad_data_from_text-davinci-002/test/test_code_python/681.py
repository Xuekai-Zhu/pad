def solution():
    beads_needed_per_bracelet = 8
    beads_available = 36
    desired_number_of_bracelets = 6
    beads_needed = desired_number_of_bracelets * beads_needed_per_bracelet - beads_available
    result = beads_needed
    
    return result

print(solution())