def solution():
    """A class is completing an art project. Each of the 30 students is assigned to a separate group and will need to take markers from the 22 boxes of markers. The first group has 10 students who will have 2 markers each and the second group has 15 students who will have 4 markers each. The last group takes the remaining markers and divides them equally. If each box of markers contains 5 markers, how many markers does each of the students in the last group receive?"""
    total_students = 30
    boxes_of_markers = 22
    markers_per_box = 5
    group1_students = 10
    group2_students = 15
    group1_markers = 2
    group2_markers = 4
    group1_total_markers = group1_students * group1_markers
    group2_total_markers = group2_students * group2_markers
    total_used_markers = group1_total_markers + group2_total_markers
    remaining_markers = (boxes_of_markers * markers_per_box) - total_used_markers
    last_group_students = total_students - group1_students - group2_students
    markers_per_student = remaining_markers // last_group_students
    result = markers_per_student
    return result

print(solution())