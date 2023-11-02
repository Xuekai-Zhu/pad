def solution():
    blue_beads = 5  # Michelle uses 5 blue beads
    red_beads = 2 * blue_beads  # Michelle uses 2 times as many red beads as blue beads
    white_beads = blue_beads + red_beads  # Michelle uses the same number of white beads as the blue and red beads combined
    total_beads = 40  # Michelle uses a total of 40 beads

    # Calculate the number of silver beads Michelle uses
    silver_beads = total_beads - (blue_beads + red_beads + white_beads)
    result = silver_beads
    return result

print(solution())