def solution():
    total_passes = 50
    right_passes = 2 * left_passes
    center_passes = left_passes + 2

    # Calculate the total number of passes to the left, right, and center
    total_side_passes = left_passes + right_passes
    total_center_passes = center_passes

    # Set up an equation to represent the total number of passes
    total_side_passes + total_center_passes = total_passes

    # Solve for the number of passes to the left
    left_passes = (total_passes - total_center_passes) / 3
    result = left_passes
    return result

print(solution())