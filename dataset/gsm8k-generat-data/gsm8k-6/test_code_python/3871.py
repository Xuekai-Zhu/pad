def solution():
    num_students = 30
    num_boxes = 22
    num_markers_per_box = 5

    # Calculate the total number of markers used by the first two groups
    group1_markers = 10 * 2
    group2_markers = 15 * 4
    total_used_markers = group1_markers + group2_markers

    # Calculate the number of markers remaining
    total_markers = num_boxes * num_markers_per_box
    remaining_markers = total_markers - total_used_markers

    # Calculate the number of markers each student in the last group receives
    num_students_last_group = num_students - 10 - 15
    markers_per_student = remaining_markers // num_students_last_group

    result = markers_per_student
    return result

print(solution())