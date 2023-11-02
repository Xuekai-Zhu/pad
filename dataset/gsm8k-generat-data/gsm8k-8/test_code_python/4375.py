def solution():
    # Define the total number of passes thrown
    total_passes = 50

    # Calculate the number of passes thrown to the right
    right_passes = total_passes / 3

    # Calculate the number of passes thrown to the center
    center_passes = right_passes + 2

    # Calculate the number of passes thrown to the left
    left_passes = total_passes - right_passes - center_passes

    result = left_passes
    return result

print(solution())