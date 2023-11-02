def solution():
    fifth_grade_students = 20
    sixth_grade_total_hours = 299
    days_in_week = 7
    winning_hours = sixth_grade_total_hours + 1
    fifth_grade_hours_needed = (winning_hours / fifth_grade_students) / days_in_week
    result = fifth_grade_hours_needed
    return result

print(solution())