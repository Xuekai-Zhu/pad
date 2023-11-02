def solution():
    """Out of 804 senior high school students, 75% passed their exams and so got their degree. The rest failed. How many didn't pass their exams?"""
    total_students = 804
    pass_percentage = 75
    fail_percentage = 100 - pass_percentage
    fail_count = (fail_percentage / 100) * total_students
    result = fail_count
    return result

print(solution())