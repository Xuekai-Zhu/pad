def solution():
    """The number of female students in the school hall is 4 times as many as the number of male students. If there are 29 male students, and there are 29 benches in the hall, at least how many students can sit on each bench for them to all fit in the hall?"""
    male_students = 29
    female_students = male_students * 4
    total_students = male_students + female_students
    benches = 29
    min_students_per_bench = (total_students + benches - 1) // benches
    result = min_students_per_bench
    return result

print(solution())