def solution():
    small_slices = 8
    large_slices = 14
    eaten_slices = 9
    num_people = 2

    # Calculate the total number of slices left
    total_slices_left = (small_slices + large_slices) - (2 * eaten_slices)

    # Calculate the number of slices per person
    slices_per_person = total_slices_left / num_people
    result = slices_per_person
    return result

print(solution())