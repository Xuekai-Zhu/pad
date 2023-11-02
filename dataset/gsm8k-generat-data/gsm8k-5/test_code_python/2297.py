def solution():
    members = 9  # There are 9 members in the crafts club
    necklaces_per_member = 2  # Each member is making 2 necklaces
    beads_per_necklace = 50  # It takes 50 beads to make each necklace

    # Calculate the total number of necklaces
    total_necklaces = members * necklaces_per_member

    # Calculate the total number of beads needed
    total_beads = total_necklaces * beads_per_necklace
    result = total_beads
    return result

print(solution())