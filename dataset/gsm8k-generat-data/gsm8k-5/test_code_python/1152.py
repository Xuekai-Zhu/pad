def solution():
    original_classes = 15
    original_students_per_class = 20
    additional_classes = 5

    # Calculate total number of students before adding more classes
    total_students_before = original_classes * original_students_per_class

    # Calculate total number of students after adding more classes
    total_classes_now = original_classes + additional_classes
    total_students_now = total_classes_now * original_students_per_class

    # Calculate the increase in number of students
    increase_in_students = total_students_now - total_students_before
    result = increase_in_students
    return result

print(solution())