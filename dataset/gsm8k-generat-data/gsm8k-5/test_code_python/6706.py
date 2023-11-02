def solution():
    total_students = 100  # Evergreen Elementary school has 100 students in Grades 4, 5, and 6
    grade_4_students = 30  # There are 30 students in Grade 4
    grade_5_students = 35  # There are 35 students in Grade 5

    # Calculate the number of students in Grade 6
    grade_6_students = total_students - grade_4_students - grade_5_students
    result = grade_6_students
    return result

print(solution())