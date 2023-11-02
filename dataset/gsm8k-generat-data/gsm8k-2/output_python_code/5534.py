def solution():
    """There are 13 3-year-olds, 20 4-year-olds, 15 5-year-olds, and 22 six-year-olds at a particular Sunday school. If the 3 and 4-year-olds are in one class and the 5 and 6-year-olds are in another class, what is the average class size?"""
    class1_size = 13 + 20
    class2_size = 15 + 22
    total_students = class1_size + class2_size
    num_classes = 2
    average_class_size = total_students / num_classes
    result = average_class_size
    return result

print(solution())