def solution():
    total_slices = 12  # The pizza had 12 slices
    john_slices = 3  # John ate 3 slices
    sam_slices = john_slices * 2  # Sam ate twice the amount that John ate
    remaining_slices = total_slices - john_slices - sam_slices  # Calculate the number of slices left

    result = remaining_slices
    return result

print(solution())