def solution():
    # Define the number of classes and students per class
    classes = 6
    students_per_class = 30

    # Calculate the total number of students
    total_students = classes * students_per_class

    # Calculate the total number of index card packs needed
    packs_needed = total_students * 2

    result = packs_needed
    return result

print(solution())