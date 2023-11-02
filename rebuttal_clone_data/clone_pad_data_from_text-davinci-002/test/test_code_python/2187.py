def solution():
    total_students = 30
    first_group = 10
    second_group = 15
    markers_per_box = 5
    markers_used = first_group * 2 + second_group * 4
    markers_left = markers_per_box * 22 - markers_used
    third_group = total_students - first_group - second_group
    markers_per_student = markers_left / third_group
    result = markers_per_student
    
    return result

print(solution())