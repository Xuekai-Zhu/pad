def solution():
    """Texas Integrated School has 15 classes and has 20 students per class. They added five more classes, how many students will they have now?"""
    # Define the initial number of classes and students per class
    initial_classes = 15
    initial_students_per_class = 20

    # Define the number of additional classes
    additional_classes = 5

    # Calculate the new total number of classes
    total_classes = initial_classes + additional_classes

    # Calculate the new total number of students
    total_students = total_classes * initial_students_per_class

    result = total_students
    return result

print(solution())