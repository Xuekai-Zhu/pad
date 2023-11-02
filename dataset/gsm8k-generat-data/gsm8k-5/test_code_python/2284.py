def solution():
    total_students = 376  # Three local dance studios have 376 students
    studio1_students = 110  # The first studio has 110 students
    studio2_students = 135  # The second studio has 135 students

    # Calculate the number of students in the third studio
    studio3_students = total_students - studio1_students - studio2_students
    result = studio3_students
    return result

print(solution())