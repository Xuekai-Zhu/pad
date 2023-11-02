def solution():
    """Nine members of the crafts club are making 2 necklaces each. It takes 50 beads to make each necklace. How many beads will they need in all?"""
    # Define the number of members in the crafts club
    members = 9

    # Define the number of necklaces each member is making
    necklaces_per_member = 2

    # Define the number of beads required to make each necklace
    beads_per_necklace = 50

    # Calculate the total number of necklaces to be made
    total_necklaces = members * necklaces_per_member

    # Calculate the total number of beads required
    total_beads = total_necklaces * beads_per_necklace

    # return the result
    result = total_beads
    return result

print(solution())