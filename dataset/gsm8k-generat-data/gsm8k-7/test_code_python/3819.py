def solution():
    total_necklaces = 50
    broken_necklaces = 3
    new_necklaces = 5
    gifted_necklaces = 15

    # Calculate the total number of necklaces after collecting unbroken beads from broken necklaces
    total_necklaces -= broken_necklaces

    # Add the new necklaces
    total_necklaces += new_necklaces

    # Subtract the gifted necklaces
    total_necklaces -= gifted_necklaces

    result = total_necklaces
    return result

print(solution())