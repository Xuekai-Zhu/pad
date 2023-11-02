def solution():
    # Calculate the total number of slices of pie
    total_slices = 2 * 8  # 2 pies sliced into 8 slices each

    # Calculate the number of slices eaten by Rebecca
    slices_eaten = 2

    # Calculate the number of slices eaten by family and friends
    slices_eaten += 0.5 * (total_slices - slices_eaten)  # 50% of the remaining slices

    # Calculate the number of slices remaining after Sunday evening
    slices_remaining = total_slices - slices_eaten - 2  # Rebecca and her husband each had another slice of pie

    result = slices_remaining
    return result

print(solution())