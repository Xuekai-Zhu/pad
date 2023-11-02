def solution():
    total_students = 80  # The school teaches 80 students
    class_A_percentage = 0.4  # 40% of the students are in class A

    # Calculate the number of students in class A
    students_in_class_A = int(total_students * class_A_percentage)

    # Calculate the number of students in class B
    students_in_class_B = students_in_class_A - 21

    # Calculate the number of students in class C
    students_in_class_C = total_students - students_in_class_A - students_in_class_B
    result = students_in_class_C
    return result

print(solution())