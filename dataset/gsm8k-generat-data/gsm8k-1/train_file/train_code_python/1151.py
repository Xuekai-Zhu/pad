def solution():
    """Texas Integrated School has 15 classes and has 20 students per class. They added five more classes, how many students will they have now?"""
    initial_classes = 15
    students_per_class = 20
    additional_classes = 5
    total_classes = initial_classes + additional_classes
    total_students = total_classes * students_per_class
    result = total_students
    return result

print(solution())