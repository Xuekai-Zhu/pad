def solution():
    # Find the total number of cake slices
    total_slices = 8 * 2 * 4  # 8 friends, each wanting 2 slices, 4 cakes
    # Subtract the number of slices Amber eats herself
    total_slices -= 3 * 2
    # Find the number of slices left over
    left_over_slices = total_slices % 6
    result = left_over_slices
    return result

print(solution())