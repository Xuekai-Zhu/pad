def solution():
    """The number of short students in a class is 2/5 of the total number of students. If there are 90 tall students, and the class has 400 students, calculate the total number of students with average height."""
    # Calculate the number of short students
    short_students = 2/5 * 400

    # Calculate the number of average-height students
    avg_height_students = 400 - short_students - 90

    # Display the number of average-height students
    result = avg_height_students
    return result

print(solution())