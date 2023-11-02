def solution():
    """Cassandra bought four dozen Granny Smith apples and used them to make four apple pies.  She cut each pie into 6 large pieces.  How many apples are in each slice of pie?"""
    # Define the number of apples and pies
    apples = 4 * 12
    pies = 4

    # Calculate the total number of apple slices
    slices = pies * 6

    # Calculate the number of apples in each slice
    apples_per_slice = apples / slices

    # Display the number of apples in each slice
    result = apples_per_slice
    return result

print(solution())