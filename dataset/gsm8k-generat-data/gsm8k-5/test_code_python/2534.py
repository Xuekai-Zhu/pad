def solution():
    pies = 2  # Rebecca bought 2 pies
    slices_per_pie = 8  # Each pie was sliced into 8 slices
    total_slices = pies * slices_per_pie  # Total number of slices
    eaten_slices = 2  # Rebecca ate 1 slice from each pie
    remaining_slices = total_slices - eaten_slices  # Rebecca and her family/friends ate 50% of the remaining slices
    remaining_slices *= 0.5
    remaining_slices -= 2  # Rebecca and her husband each had another slice on Sunday evening

    result = remaining_slices
    return result

print(solution())