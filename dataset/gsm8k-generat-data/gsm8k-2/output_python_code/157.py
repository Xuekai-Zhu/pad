def solution():
    """A young girl pours 23 blue beads and 16 yellow beads into a bowl. She divides the total into 3 equal parts, removes some beads from each part, and doubles the rest to have 6 beads in each part now. How many beads were removed from each part?"""
    total_beads = 23 + 16
    each_part = total_beads / 3
    remaining_beads = each_part / 2
    removed_beads = each_part - remaining_beads
    result = removed_beads
    return result

print(solution())