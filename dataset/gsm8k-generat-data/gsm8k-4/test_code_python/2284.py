def solution():
    """Three local dance studios have 376 students. The first two have 110 and 135 students. How many students does the third studio have?"""
    # Define the total number of students and the number of students in the first two studios
    total_students = 376
    first_two_studios = 110 + 135

    # Calculate the number of students in the third studio
    third_studio = total_students - first_two_studios

    result = third_studio
    return result

print(solution())