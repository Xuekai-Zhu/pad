def solution():
    num_members = 9
    num_necklaces_per_member = 2
    num_beads_per_necklace = 50

    # Calculate the total number of necklaces that will be made
    total_necklaces = num_members * num_necklaces_per_member

    # Calculate the total number of beads needed for all necklaces
    total_beads = total_necklaces * num_beads_per_necklace
    result = total_beads
    return result

print(solution())