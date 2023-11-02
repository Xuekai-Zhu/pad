def solution():
    """Joey studies for his SAT exams 2 hours per night 5 nights a week. On the weekends, he studies 3 hours a day. If his SAT exam is 6 weeks away, how much time will Joey spend studying?"""
    week_days = 5
    weekend_days = 2
    nightly_hours = 2
    weekend_hours = 3
    total_weeks = 6
    total_weekday_hours = nightly_hours * week_days
    total_weekend_hours = weekend_hours * weekend_days
    total_study_hours = (total_weekday_hours + total_weekend_hours) * total_weeks
    result = total_study_hours
    return result

print(solution())