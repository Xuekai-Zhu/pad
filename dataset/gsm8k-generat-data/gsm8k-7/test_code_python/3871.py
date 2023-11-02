def solution():
    num_students = 30
    num_boxes = 22
    num_markers_per_box = 5

    # Calculate the total number of markers needed by the first two groups
    num_markers_first_group = 10 * 2
    num_markers_second_group = 15 * 4
    total_markers_used = num_markers_first_group + num_markers_second_group

    # Calculate the number of markers remaining
    num_markers_remaining = num_boxes * num_markers_per_box - total_markers_used

    # Calculate the number of markers each student in the last group receives
    num_students_last_group = num_students - 10 - 15
    num_markers_each_last_group_student = num_markers_remaining // num_students_last_group
    result = num_markers_each_last_group_student
    return result

print(solution())