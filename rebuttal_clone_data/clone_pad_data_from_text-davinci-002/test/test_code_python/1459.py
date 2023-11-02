def solution():
    weekly_hours = 48
    number_of_courses = 4
    number_of_weeks = 4
    hourly_rate = 25
    hours_per_course = weekly_hours / number_of_courses
    total_hours = hours_per_course * number_of_weeks
    total_earnings = hourly_rate * total_hours
    result = total_earnings
    return result

print(solution())