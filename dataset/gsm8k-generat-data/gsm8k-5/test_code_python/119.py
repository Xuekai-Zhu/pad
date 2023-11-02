def solution():
    students_per_class = 30  # Each fourth-grade class has 30 students
    num_classes = 3  # There are 3 fourth-grade classes
    num_PE_students = 50  # There are 50 students in the P.E. class

    # Calculate the total number of cupcakes needed for the fourth-grade classes
    cupcakes_for_fourth_grade = students_per_class * num_classes

    # Calculate the total number of cupcakes needed for all students
    total_cupcakes = cupcakes_for_fourth_grade + num_PE_students
    result = total_cupcakes
    return result

print(solution())