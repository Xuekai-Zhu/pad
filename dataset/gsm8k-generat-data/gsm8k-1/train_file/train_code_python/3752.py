def solution():
    """Out of 804 senior high school students, 75% passed their exams and so got their degree. The rest failed. How many didn't pass their exams?"""
    total_students = 804
    pass_percent = 75
    pass_students = int(total_students * (pass_percent/100))
    fail_students = total_students - pass_students
    result = fail_students
    return result

print(solution())