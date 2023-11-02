def solution():
    # Define the total number of slices in the loaf
    total_slices = 12

    # Calculate the number of slices eaten for breakfast
    breakfast_slices = total_slices // 3

    # Calculate the number of slices remaining after breakfast
    remaining_slices = total_slices - breakfast_slices

    # Calculate the number of slices remaining after making a sandwich for lunch
    remaining_slices -= 2

    result = remaining_slices
    return result

print(solution())