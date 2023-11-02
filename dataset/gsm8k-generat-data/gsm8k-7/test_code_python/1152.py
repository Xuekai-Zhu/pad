def solution():
    num_classes = 15
    students_per_class = 20
    additional_classes = 5

    # Calculate the total number of classes after adding more classes
    total_classes = num_classes + additional_classes

    # Calculate the total number of students with the added classes
    total_students = total_classes * students_per_class
    result = total_students
    return result

print(solution())