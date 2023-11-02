def solution():
    # Calculate the number of short students
    short_students = (2/5) * 400  # 2/5 of the total number of students

    # Calculate the number of students with average height
    avg_height_students = 400 - short_students - 90  # total students minus short students and tall students

    result = avg_height_students
    return result

print(solution())