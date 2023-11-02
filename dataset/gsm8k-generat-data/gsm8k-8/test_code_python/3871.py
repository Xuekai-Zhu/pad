def solution():
    # Calculate the total number of markers needed by the first two groups
    total_markers_used = (10 * 2) + (15 * 4)

    # Calculate the total number of markers remaining
    markers_remaining = (30 * 22) - total_markers_used

    # Calculate the number of markers each student in the last group receives
    last_group_size = 30 - 10 - 15
    markers_per_student = markers_remaining // last_group_size

    result = markers_per_student
    return result

print(solution())