def solution():
    # Find the number of female students in the hall
    female_students = 4 * 29

    # Find the total number of students in the hall
    total_students = 29 + female_students

    # Find the minimum number of students that can sit on each bench
    students_per_bench = total_students // 29

    result = students_per_bench
    return result

print(solution())