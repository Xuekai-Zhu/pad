def solution():
    # Calculate the total number of slices and pieces of bell pepper
    large_slices = 5 * 20  # 5 bell peppers cut into 20 large slices each
    small_pieces = (5 * 20 * 0.5) * 3  # half of the slices cut into 3 smaller pieces each
    total_slices = large_slices + small_pieces
    result = total_slices
    return result

print(solution())