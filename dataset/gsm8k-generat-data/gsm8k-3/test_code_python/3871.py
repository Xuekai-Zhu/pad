def solution():
    """A class is completing an art project. Each of the 30 students is assigned to a separate group and will need to take markers from the 22 boxes of markers. The first group has 10 students who will have 2 markers each and the second group has 15 students who will have 4 markers each. The last group takes the remaining markers and divides them equally. If each box of markers contains 5 markers, how many markers does each of the students in the last group receive?"""
    # Define the total number of students and boxes of markers
    TOTAL_STUDENTS = 30
    TOTAL_BOXES = 22
    MARKERS_PER_BOX = 5

    # Calculate the number of markers needed for the first group
    group1_students = 10
    group1_markers = 2
    group1_total_markers = group1_students * group1_markers

    # Calculate the number of markers needed for the second group
    group2_students = 15
    group2_markers = 4
    group2_total_markers = group2_students * group2_markers

    # Calculate the total number of markers used by the first two groups
    total_used_markers = group1_total_markers + group2_total_markers

    # Calculate the remaining number of boxes of markers
    remaining_boxes = TOTAL_BOXES - (group1_students + group2_students)

    # Calculate the total number of markers in the remaining boxes
    remaining_markers = remaining_boxes * MARKERS_PER_BOX

    # Calculate the number of markers each student in the last group receives
    last_group_students = TOTAL_STUDENTS - (group1_students + group2_students)
    markers_per_student = remaining_markers // last_group_students

    # Display the number of markers each student in the last group receives
    result = markers_per_student
    return result

print(solution())