def solution():
    # Calculate the total number of slices of bread Tony used
    total_slices_used = 2 * 6 + 4  # two sandwiches for 6 days and two sandwiches on Saturday
    slices_left = 22 - total_slices_used  # Calculate the number of slices left from the 22-slice loaf
    result = slices_left
    return result

print(solution())