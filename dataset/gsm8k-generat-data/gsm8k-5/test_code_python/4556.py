def solution():
    fifth_grade_students = 20  # The fifth grade has 20 students
    sixth_grade_total_hours = 299  # The 6th grade read a total of 299 hours
    sixth_grade_average_hours = sixth_grade_total_hours / fifth_grade_students  # Find the 6th grade's average hours per student
    required_average = sixth_grade_average_hours + 1  # The 5th grade needs to average 1 hour more than the 6th grade to win

    days_in_week = 7  # There are 7 days in a week
    required_total_hours = required_average * fifth_grade_students * days_in_week  # Calculate total hours needed to win
    required_hours_per_day = required_total_hours / (fifth_grade_students * days_in_week)  # Calculate required hours per day

    result = required_hours_per_day
    return result

print(solution())