def solution():
    """A class is completing an art project. Each of the 30 students is assigned to a separate group and will need to take markers from the 22 boxes of markers. The first group has 10 students who will have 2 markers each and the second group has 15 students who will have 4 markers each. The last group takes the remaining markers and divides them equally. If each box of markers contains 5 markers, how many markers does each of the students in the last group receive?"""
    # Define the number of students and boxes of markers
    NUM_STUDENTS = 30
    NUM_BOXES_MARKERS = 22
    MARKERS_PER_BOX = 5

    # Define the number of students and markers for the first group
    group1_num_students = 10
    group1_num_markers = 2

    # Calculate the number of markers used by the first group
    group1_markers_used = group1_num_students * group1_num_markers

    # Define the number of students and markers for the second group
    group2_num_students = 15
    group2_num_markers = 4

    # Calculate the number of markers used by the second group
    group2_markers_used = group2_num_students * group2_num_markers

    # Calculate the total number of markers used by the first two groups
    total_markers_used = group1_markers_used + group2_markers_used

    # Calculate the remaining number of markers
    remaining_markers = NUM_BOXES_MARKERS * MARKERS_PER_BOX - total_markers_used

    # Calculate the number of markers each student in the last group receives
    last_group_num_students = NUM_STUDENTS - group1_num_students - group2_num_students
    markers_per_student = remaining_markers / last_group_num_students

    # return the result
    result = markers_per_student
    return result

print(solution())