def solution():
    num_apples = 4 * 12  # 4 dozen apples
    num_pies = 4

    # Each pie is cut into 6 large pieces, so each piece contains 1/6th of a pie
    num_slices = num_pies * 6

    # Calculate the number of apples per slice by dividing the total number of apples by the number of slices
    apples_per_slice = num_apples / num_slices
    result = apples_per_slice
    return result

print(solution())