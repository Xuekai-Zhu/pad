def solution():
    """The number of short students in a class is 2/5 of the total number of students. If there are 90 tall students, and the class has 400 students, calculate the total number of students with average height."""
    # Define the total number of students and the number of tall students
    total_students = 400
    tall_students = 90

    # Calculate the number of short students
    short_students = int(total_students * (2/5))

    # Calculate the number of average height students
    average_students = total_students - short_students - tall_students

    # Return the result
    result = average_students
    return result

print(solution())