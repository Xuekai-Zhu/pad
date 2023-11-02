def solution():
    """Mabel has 5 daisies in her garden, and each daisy has 8 petals.  If she gives 2 daisies to her teacher, how many petals does she have on the remaining daisies in her garden?"""
    # Define the number of daisies and petals per daisy
    DAISIES = 5
    PETALS_PER_DAISY = 8

    # Calculate the total number of petals
    total_petals = DAISIES * PETALS_PER_DAISY

    # Subtract the petals from the two daisies given away
    total_petals -= 2 * PETALS_PER_DAISY

    # Calculate the number of petals on the remaining daisies
    remaining_petals = total_petals / 3

    # Display the number of petals on the remaining daisies
    result = remaining_petals
    return result

print(solution())