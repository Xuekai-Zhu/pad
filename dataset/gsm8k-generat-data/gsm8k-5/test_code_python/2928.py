def solution():
    num_teachers = 48
    num_principal = 1
    num_classes = 15
    num_students_per_class = 20

    # Calculate the number of students in the school
    num_students = num_classes * num_students_per_class

    # Calculate the total number of people in the school
    total_people = num_teachers + num_principal + num_students
    result = total_people
    return result

print(solution())