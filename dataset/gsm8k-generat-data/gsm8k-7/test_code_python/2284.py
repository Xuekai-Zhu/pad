def solution():
    total_students = 376
    studio1_students = 110
    studio2_students = 135

    # Calculate the number of students in the third studio
    studio3_students = total_students - studio1_students - studio2_students
    result = studio3_students
    return result

print(solution())