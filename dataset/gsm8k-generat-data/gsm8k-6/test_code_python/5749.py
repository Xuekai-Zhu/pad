def solution():
    # Calculate the total number of slices
    total_slices = 3 * 8  # each pizza is cut into 8 slices
    slices_per_person = total_slices // 12  # divide the slices equally among the 12 coworkers
    result = slices_per_person
    return result

print(solution())