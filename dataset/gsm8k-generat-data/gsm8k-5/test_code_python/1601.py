def solution():
    short_students = 2/5 * 400  # Calculate the number of short students in the class
    total_tall_students = 90  # Given
    total_students = 400  # Given

    # Calculate the number of average height students
    average_height_students = total_students - short_students - total_tall_students
    result = average_height_students
    return result

print(solution())