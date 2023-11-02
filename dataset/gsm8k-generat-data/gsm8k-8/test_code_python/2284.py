def solution():
    # Define the number of students in the first two studios
    studio1_students = 110
    studio2_students = 135

    # Calculate the total number of students in the first two studios
    total_students = studio1_students + studio2_students

    # Calculate the number of students in the third studio
    third_studio_students = 376 - total_students
    result = third_studio_students
    return result

print(solution())