def solution():
    
    total_beads = 40
    blue_beads = 5
    red_beads = 2 * blue_beads
    white_beads = blue_beads + red_beads
    used_beads = blue_beads + red_beads + white_beads
    silver_beads = total_beads - used_beads
    result = silver_beads
    return result

print(solution())