def solution():
    # Calculate the number of cake slices kept
    slices_kept = 12 - (12 * 1/4)  # only one-fourth of the cake was eaten, so three-fourths of the cake (9 slices) were kept
    result = slices_kept
    return result

print(solution())