def solution():
    """John buys 2 packs of index cards for all his students. He has 6 classes and 30 students in each class. How many packs did he buy?"""
    # Define the number of classes and students per class
    num_classes = 6
    students_per_class = 30

    # Calculate the total number of students
    total_students = num_classes * students_per_class

    # Calculate the total number of packs needed
    total_packs = total_students * 2

    # return the result
    result = total_packs
    return result

print(solution())