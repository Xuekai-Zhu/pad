def solution():
    # Define the size ratios
    full_size = 240
    mid_size_ratio = 1/10
    small_size_ratio = 1/2

    # Calculate the length of the mid-size model
    mid_size = full_size * mid_size_ratio

    # Calculate the length of the smallest model
    small_size = mid_size * small_size_ratio

    result = small_size
    return result

print(solution())