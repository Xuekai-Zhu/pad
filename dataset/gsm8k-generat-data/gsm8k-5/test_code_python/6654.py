def solution():
    packs_per_student = 2  # John buys 2 packs of index cards for each student
    classes = 6  # John has 6 classes
    students_per_class = 30  # Each class has 30 students

    # Calculate the total number of packs John bought
    total_packs = packs_per_student * classes * students_per_class
    result = total_packs
    return result

print(solution())