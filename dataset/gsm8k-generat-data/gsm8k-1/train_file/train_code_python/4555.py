def solution():
    """The school is having a book-a-thon. The winning class gets a pizza party. The fifth grade has 20 students and one week to read as much as possible. The 6th grade already finished and read a total of 299 hours. How many hours does each student in 5th grade need to average per day to beat them by 1?"""
    fifth_grade_students = 20
    sixth_grade_hours = 299
    week_days = 7
    hours_to_beat = 300
    hours_per_day = (hours_to_beat - sixth_grade_hours) / (fifth_grade_students * week_days)
    result = hours_per_day
    return result

print(solution())