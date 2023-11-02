def solution():
    # Calculate the number of female students
    female_students = 4 * 29  # 4 times as many female students as male students

    # Calculate the total number of students in the hall
    total_students = female_students + 29  # Total number of female and male students

    # Calculate the minimum number of students per bench for all to fit
    students_per_bench = (total_students // 29) + 1  # Round up to ensure all students can sit

    result = students_per_bench
    return result

print(solution())