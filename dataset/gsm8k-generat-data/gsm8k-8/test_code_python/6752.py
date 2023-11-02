def solution():
    # Define the number of apples and pies
    apples = 4*12
    pies = 4

    # Determine the total number of slices
    total_slices = pies * 6

    # Calculate the number of apples in each slice
    apples_per_slice = apples / total_slices

    result = apples_per_slice
    return result

print(solution())