def solution():
    # Calculate the number of students from Karen High School
    karen_students = (3/5) * 50

    # Calculate the combined number of students from Know It All and Karen High School
    know_and_karen = 50 + karen_students

    # Calculate the number of students from Novel Corona High School
    novel_corona_students = 2 * know_and_karen

    # Calculate the total number of students at the competition
    total_students = 50 + karen_students + novel_corona_students

    result = total_students
    return result

print(solution())