def solution():
    """Calculate the total number of students at a science fair competition."""
    # Define the number of students from Know It All High School
    know_it_all_students = 50

    # Define the ratio of Karen High students to Know It All High students
    karen_ratio = 3/5

    # Calculate the number of students from Karen High School
    karen_students = karen_ratio * know_it_all_students

    # Calculate the combined number of students from Know It All and Karen High Schools
    know_it_all_and_karen_students = know_it_all_students + karen_students

    # Calculate the number of students from Novel Corona High School
    novel_corona_students = 2 * know_it_all_and_karen_students

    # Calculate the total number of students at the competition
    total_students = know_it_all_students + karen_students + novel_corona_students

    result = total_students
    return result

print(solution())