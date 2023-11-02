def solution():
    """The number of female students in the school hall is 4 times as many as the number of male students. If there are 29 male students, and there are 29 benches in the hall, at least how many students can sit on each bench for them to all fit in the hall?"""
    # Define the number of male students and benches
    male_students = 29
    benches = 29

    # Calculate the number of female students
    female_students = male_students * 4

    # Calculate the total number of students
    total_students = male_students + female_students

    # Calculate the minimum number of students per bench
    students_per_bench = total_students // benches

    result = students_per_bench
    return result

print(solution())