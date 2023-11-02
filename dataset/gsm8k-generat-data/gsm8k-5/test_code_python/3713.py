def solution():
    # Calculate the number of cake slices that were eaten
    eaten_slices = 12 * 0.25

    # Subtract the eaten slices from the total number of slices to get the number of slices that were kept
    kept_slices = 12 - eaten_slices
    result = kept_slices
    return result

print(solution())