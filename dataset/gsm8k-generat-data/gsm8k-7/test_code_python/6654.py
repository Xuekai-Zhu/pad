def solution():
    num_classes = 6
    num_students_per_class = 30
    num_packs_per_student = 2

    # Calculate the total number of students
    total_students = num_classes * num_students_per_class

    # Calculate the total number of packs
    total_packs = total_students * num_packs_per_student
    result = total_packs
    return result

print(solution())