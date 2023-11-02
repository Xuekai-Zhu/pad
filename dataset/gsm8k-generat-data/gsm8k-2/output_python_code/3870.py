def solution():
    """A class is completing an art project. Each of the 30 students is assigned to a separate group and will need to take markers from the 22 boxes of markers. The first group has 10 students who will have 2 markers each and the second group has 15 students who will have 4 markers each. The last group takes the remaining markers and divides them equally. If each box of markers contains 5 markers, how many markers does each of the students in the last group receive?"""
    total_students = 30
    total_boxes = 22
    markers_per_box = 5
    first_group_students = 10
    first_group_markers = 2
    second_group_students = 15
    second_group_markers = 4
    remaining_boxes = total_boxes - (first_group_students + second_group_students)
    remaining_markers = remaining_boxes * markers_per_box
    total_markers_needed = (first_group_students * first_group_markers) + (second_group_students * second_group_markers)
    markers_left = remaining_markers - total_markers_needed
    students_left = total_students - (first_group_students + second_group_students)
    markers_per_student = markers_left / students_left
    result = markers_per_student
    return result

print(solution())