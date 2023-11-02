def solution():
    """Nine members of the crafts club are making 2 necklaces each. It takes 50 beads to make each necklace. How many beads will they need in all?"""
    members = 9
    necklaces_per_member = 2
    beads_per_necklace = 50
    total_beads = members * necklaces_per_member * beads_per_necklace
    result = total_beads
    return result

print(solution())