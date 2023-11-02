def solution():
    harrison_students = 1590
    moving_students = harrison_students * .40
    total_classes = 3 * 7
    normal_classes = total_classes - 1
    students_per_class = moving_students / normal_classes
    result = students_per_class
    return result

print(solution())