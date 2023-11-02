def solution():
    blue_beads = 5
    red_beads = blue_beads * 2
    white_beads = blue_beads + red_beads
    silver_beads = 40 - (blue_beads + red_beads + white_beads)
    result = silver_beads
    return result

print(solution())