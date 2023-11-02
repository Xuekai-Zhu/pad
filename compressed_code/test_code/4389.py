def solution():
    
    num_students_group1 = 9
    num_students_group2 = 10
    num_students_group3 = 11
    num_tissues_per_box = 40
    total_num_students = num_students_group1 + num_students_group2 + num_students_group3
    total_num_boxes = total_num_students // 1  
    total_num_tissues = total_num_boxes * num_tissues_per_box
    result = total_num_tissues
    return result

print(solution())