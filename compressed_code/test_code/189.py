def solution():
    
    total_students = 80
    class_a_percent = 0.4
    class_a_students = total_students * class_a_percent
    class_b_students = class_a_students - 21
    class_c_students = total_students - class_a_students - class_b_students
    result = class_c_students
    return result

print(solution())