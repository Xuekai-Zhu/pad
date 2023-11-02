def solution():
    """The number of short students in a class is 2/5 of the total number of students. If there are 90 tall students, and the class has 400 students, calculate the total number of students with average height."""
    total_students = 400
    tall_students = 90
    short_students = (2/5) * total_students
    avg_height_students = total_students - tall_students - short_students
    result = avg_height_students
    return result

print(solution())