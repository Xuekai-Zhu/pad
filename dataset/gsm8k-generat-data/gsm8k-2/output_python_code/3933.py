def solution():
    """Janet goes to the gym for 5 hours a week. She goes Monday, Tuesday, Wednesday, and Friday. She spends an hour and a half each day on Monday and Wednesday. If she spends the same amount of time at the gym on Tuesday and Friday how many hours is she at the gym on Friday?"""
    total_weekly_hours = 5
    monday_and_wednesday_hours = 1.5 + 1.5
    tuesday_and_friday_hours = (total_weekly_hours - monday_and_wednesday_hours) / 2
    friday_hours = tuesday_and_friday_hours
    result = friday_hours
    return result

print(solution())