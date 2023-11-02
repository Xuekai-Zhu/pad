def solution():
    
    num_classes = 40
    num_students_per_class = 25
    num_teachers_per_class = 3
    num_trees_per_child = 1
    num_trees_per_teacher = 2
    total_students = num_classes * num_students_per_class
    total_teachers = num_classes * num_teachers_per_class
    total_trees = total_students * num_trees_per_child + total_teachers * num_trees_per_teacher
    result = total_trees
    return result

print(solution())