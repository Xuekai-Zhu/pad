def solution():
    # Calculate the number of slices James eats
    total_slices = 8 * 2  # 8 pieces of pizza with 2 slices each
    friend_slices = 2  # friend eats 2 slices
    remaining_slices = total_slices - friend_slices  # James has the remaining slices
    james_slices = remaining_slices // 2  # James eats half of the remaining slices
    result = james_slices
    return result

print(solution())