def solution():
    """At Ashley's school, they start a reforestation campaign where each child plants a tree and each teacher plants 2 trees. The school has 40 classes with an average of 25 students and 3 teachers per class. How many trees will they have planted at the end of the campaign?"""
    students_per_class = 25
    teachers_per_class = 3
    classes = 40
    trees_per_student = 1
    trees_per_teacher = 2
    total_students = students_per_class * classes
    total_teachers = teachers_per_class * classes
    total_student_trees = total_students * trees_per_student
    total_teacher_trees = total_teachers * trees_per_teacher
    total_trees = total_student_trees + total_teacher_trees
    result = total_trees

    return result

print(solution())