def solution():
    """Ruth goes to school 8 hours a day and 5 days a week. She is in math class 25% of this time. How many hours per week does she spend in math class?"""
    daily_hours = 8
    weekly_days = 5
    math_percentage = 0.25
    math_hours_per_day = daily_hours * math_percentage
    math_hours_per_week = math_hours_per_day * weekly_days
    result = math_hours_per_week
    return result

print(solution())