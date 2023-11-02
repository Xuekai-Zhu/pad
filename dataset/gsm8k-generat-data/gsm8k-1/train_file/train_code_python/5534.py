def solution():
    """There are 13 3-year-olds, 20 4-year-olds, 15 5-year-olds, and 22 six-year-olds at a particular Sunday school. If the 3 and 4-year-olds are in one class and the 5 and 6-year-olds are in another class, what is the average class size?"""
    class_1_size = 13 + 20
    class_2_size = 15 + 22
    average_class_size = (class_1_size + class_2_size) / 2
    result = average_class_size
    return result

print(solution())