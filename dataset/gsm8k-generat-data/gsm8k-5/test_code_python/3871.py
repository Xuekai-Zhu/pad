def solution():
    total_students = 30  # There are 30 students in the class
    total_boxes = 22  # There are 22 boxes of markers
    markers_per_box = 5  # Each box has 5 markers
    first_group_size = 10  # The first group has 10 students
    second_group_size = 15  # The second group has 15 students

    # Calculate the total number of markers used by the first two groups
    markers_used = (2 * first_group_size) + (4 * second_group_size)

    # Calculate the total number of markers remaining
    markers_remaining = total_boxes * markers_per_box - markers_used

    # Calculate the number of markers each student in the last group receives
    last_group_size = total_students - first_group_size - second_group_size
    markers_per_student = markers_remaining // last_group_size

    result = markers_per_student
    return result

print(solution())