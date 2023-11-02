def solution():
     """A young girl pours 23 blue beads and 16 yellow beads into a bowl. She divides the total into 3 equal parts, removes some beads from each part, and doubles the rest to have 6 beads in each part now. How many beads were removed from each part?"""
     blue_beads = 23
     yellow_beads = 16
     total_beads = blue_beads + yellow_beads
     beads_removed = (total_beads / 3) - 6
     result = beads_removed
     return result

print(solution())