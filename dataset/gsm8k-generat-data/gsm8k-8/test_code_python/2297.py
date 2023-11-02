def solution():
    # Define the number of members and necklaces per member
    members = 9
    necklaces_per_member = 2

    # Calculate the total number of necklaces
    total_necklaces = members * necklaces_per_member

    # Calculate the total number of beads needed
    beads_per_necklace = 50
    total_beads = total_necklaces * beads_per_necklace
    result = total_beads
    return result

print(solution())