def solution():
    
    # Define the number of students and teachers per class
    students_per_class = 25
    teachers_per_class = 3

    # Define the number of classes and the number of trees per student and teacher
    num_classes = 40
    trees_per_student = 1
    trees_per_teacher = 2

    # Calculate the total number of trees planted
    total_trees = (students_per_class * trees_per_student) + (teachers_per_class * trees_per_teacher)

    # return the result
    result = total_trees
    return result

print(solution())