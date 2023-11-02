def solution():
    """The number of female students in the school hall is 4 times as many as the number of male students. If there are 29 male students, and there are 29 benches in the hall, at least how many students can sit on each bench for them to all fit in the hall?"""
    # Find the number of female students
    female_students = 4 * 29

    # Calculate the total number of students
    total_students = female_students + 29

    # Calculate the minimum number of students that can sit on each bench
    min_students_per_bench = total_students // 29

    # Display the result
    result = min_students_per_bench
    return result

print(solution())