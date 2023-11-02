def solution():
    """Three local dance studios have 376 students. The first two have 110 and 135 students. How many students does the third studio have?"""
    # Define the number of students in the first two studios
    studio1_students = 110
    studio2_students = 135

    # Calculate the number of students in the third studio
    studio3_students = 376 - studio1_students - studio2_students

    # Display the number of students in the third studio
    result = studio3_students
    return result

print(solution())