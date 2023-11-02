def solution():
    # Calculate the number of beads from broken necklaces
    beads_from_broken = 3 * (50 / 3)  # There are 50 necklaces in total, and 3 are broken

    # Calculate the number of necklaces remaining after breaking apart the 3 broken ones
    remaining_necklaces = 50 - 3

    # Calculate the total number of necklaces after buying 5 new ones and giving away 15
    total_necklaces = remaining_necklaces + 5 - 15
    result = total_necklaces
    return result

print(solution())