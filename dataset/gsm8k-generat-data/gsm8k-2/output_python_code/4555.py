def solution():
    """The school is having a book-a-thon. The winning class gets a pizza party. 
       The fifth grade has 20 students and one week to read as much as possible. 
       The 6th grade already finished and read a total of 299 hours. 
       How many hours does each student in 5th grade need to average per day to beat them by 1?"""
    fifth_grade_students = 20
    sixth_grade_total_hours = 299
    week_in_days = 7
    hours_per_day_to_win_by_1 = (sixth_grade_total_hours / week_in_days + 1 - (fifth_grade_students * 0.01)) / fifth_grade_students
    result = hours_per_day_to_win_by_1
    return result

print(solution())