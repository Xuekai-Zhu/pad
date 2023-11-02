def solution():
    """John buys 2 packs of index cards for all his students. He has 6 classes and 30 students in each class. How many packs did he buy?"""
    packs_per_student = 2
    classes = 6
    students_per_class = 30
    total_students = classes * students_per_class
    packs_bought = packs_per_student * total_students
    result = packs_bought
    return result

print(solution())