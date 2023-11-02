def solution():
    """In a batch of 30 apples, 1/6 are too small and 1/3 are not ripe.  The others are perfect. Calculate the number of perfect apples."""
    # Define the total number of apples
    total_apples = 30

    # Calculate the number of apples that are too small
    small_apples = total_apples * (1/6)

    # Calculate the number of apples that are not ripe
    not_ripe_apples = total_apples * (1/3)

    # Calculate the number of perfect apples
    perfect_apples = total_apples - small_apples - not_ripe_apples

    # return the result
    result = perfect_apples
    return result

print(solution())