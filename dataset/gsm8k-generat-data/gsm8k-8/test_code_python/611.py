def solution():
    # Calculate the total number of slices after cutting the pizza
    total_slices = 40 / 2 / 2

    # Calculate the number of slices on the slice given to Jelly
    jelly_slice_slices = total_slices / 4 - 1

    result = jelly_slice_slices
    return result

print(solution())