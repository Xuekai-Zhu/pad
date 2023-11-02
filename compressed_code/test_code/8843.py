def solution():
    
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