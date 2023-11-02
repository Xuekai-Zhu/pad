def solution():
    monthly_rent = 500
    daily_food = 10
    weekly_lessons = 60
    lessons_per_week = 2
    weeks_per_month = 4
    months_per_year = 12

    monthly_expenses = monthly_rent + (daily_food * days_per_month) + (weekly_lessons * lessons_per_week)
    yearly_expenses = monthly_expenses * months_per_year
    result = yearly_expenses

    return result

print(solution())