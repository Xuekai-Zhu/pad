def solution():
    
    sandwiches_per_student = 2
    students_per_group = 6
    total_groups = 5
    total_students = students_per_group * total_groups
    total_sandwiches = sandwiches_per_student * total_students
    total_bread_slices = total_sandwiches * 2
    result = total_bread_slices
    return result

print(solution())