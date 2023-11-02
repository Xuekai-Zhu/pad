def solution():
    """John buys 2 packs of index cards for all his students. He has 6 classes and 30 students in each class. How many packs did he buy?"""
    students_per_class = 30
    num_classes = 6
    packs_per_student = 2
    total_students = students_per_class * num_classes
    total_packs = total_students * packs_per_student
    result = total_packs
    return result

print(solution())