def solution():
    total_students = 80
    class_a_percentage = 0.4
    class_b_difference = 21

    # Calculate the number of students in class A
    num_class_a = total_students * class_a_percentage

    # Calculate the number of students in class B
    num_class_b = num_class_a - class_b_difference

    # Calculate the number of students in class C
    num_class_c = total_students - num_class_a - num_class_b

    result = num_class_c
    return result

print(solution())