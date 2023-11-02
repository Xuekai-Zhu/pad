def solution():
    days_in_week = 7
    weekends_in_week = 2
    hours_spent_on_weekends = 3 * days_in_week
    hours_spent_on_weekdays = 4 * days_in_week
    hours_spent_ facebooking = 3
    hours_spent_working = hours_spent_on_weekdays - hours_spent_ facebooking
    total_hours_spent_working = hours_spent_working + hours_spent_on_weekends
    return total_hours_spent_working

print(solution())