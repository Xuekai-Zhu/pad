def solution():
    # Calculate the number of unbroken beads collected from the broken necklaces
    unbroken_beads = 3 * (10 - 1)  # Each necklace has 10 beads, 1 bead is broken, so 9 unbroken beads per necklace

    # Calculate the total number of necklaces after throwing away the broken ones and adding new ones
    total_necklaces = 50 - 3 + 5

    # Calculate the number of necklaces remaining after giving 15 as gifts
    remaining_necklaces = total_necklaces - 15

    result = remaining_necklaces
    return result

print(solution())