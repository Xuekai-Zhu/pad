def solution():
    # Define the initial number of classes and students per class
    initial_classes = 15
    initial_students_per_class = 20

    # Calculate the initial total number of students
    initial_total_students = initial_classes * initial_students_per_class

    # Define the number of additional classes
    additional_classes = 5

    # Calculate the new total number of students
    new_total_students = (initial_classes + additional_classes) * initial_students_per_class

    # Calculate the increase in number of students
    increase_in_students = new_total_students - initial_total_students

    result = increase_in_students
    return result

print(solution())