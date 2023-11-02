def solution():
    """Nine members of the crafts club are making 2 necklaces each. It takes 50 beads to make each necklace. How many beads will they need in all?"""
    # Define the number of members and necklaces per member
    members = 9
    necklaces_per_member = 2

    # Define the number of beads per necklace
    beads_per_necklace = 50

    # Calculate the total number of beads needed
    total_beads = members * necklaces_per_member * beads_per_necklace

    # Display the total number of beads
    result = total_beads
    return result

print(solution())