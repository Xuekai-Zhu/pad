def solution():
    """A young girl pours 23 blue beads and 16 yellow beads into a bowl. She divides the total into 3 equal parts, removes some beads from each part, and doubles the rest to have 6 beads in each part now. How many beads were removed from each part?"""
    total_beads = 23 + 16
    parts = 3
    beads_per_part = total_beads / parts
    final_beads_per_part = 6
    removed_beads_per_part = (beads_per_part - final_beads_per_part) * 2
    result = removed_beads_per_part
    return result

print(solution())