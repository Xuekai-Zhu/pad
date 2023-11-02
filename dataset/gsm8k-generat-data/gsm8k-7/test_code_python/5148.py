def solution():
    first_class_students = 20
    second_and_third_class_students = 25
    fourth_class_students = first_class_students / 2
    fifth_and_sixth_class_students = 28

    # Calculate the total number of students in all classes
    total_students = (first_class_students + (2 * second_and_third_class_students) + fourth_class_students +
                       (2 * fifth_and_sixth_class_students))

    # Calculate the total number of classes
    total_classes = 6

    # Calculate the average number of students Monica sees per day
    num_students_per_day = total_students / total_classes
    result = num_students_per_day
    return result

print(solution())