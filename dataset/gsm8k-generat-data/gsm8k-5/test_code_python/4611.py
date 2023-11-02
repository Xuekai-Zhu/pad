def solution():
    # Calculate the number of students that joined Hendrix's class at the beginning of the year
    initial_students = 160

    # Calculate the number of students that joined the class during the year
    new_students = 20

    # Calculate the number of students that remained in the class at the end of the year
    remaining_students = (2/3) * (initial_students + new_students)

    result = remaining_students
    return result

print(solution())