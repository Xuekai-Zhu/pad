def solution():
    # Calculate the number of female students
    female_students = 4 * 29

    # Calculate the total number of students
    total_students = female_students + 29

    # Calculate the minimum number of students per bench
    min_students_per_bench = total_students // 29

    result = min_students_per_bench
    return result

print(solution())