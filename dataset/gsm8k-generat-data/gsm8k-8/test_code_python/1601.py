def solution():
    # Calculate the number of short students
    short_students = 2/5 * 400

    # Calculate the total number of students with average height
    average_height_students = 400 - 90 - short_students
    result = average_height_students
    return result

print(solution())