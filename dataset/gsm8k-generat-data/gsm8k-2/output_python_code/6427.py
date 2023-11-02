def solution():
    """Percy swims 1 hour before school and 1 after school 5 days a week. He swims 3 hours on the weekend. How many hours of swimming does he do over 4 weeks?"""
    weekday_swimming_hours = 1 + 1  # before and after school
    weekly_swimming_hours = (weekday_swimming_hours * 5) + 3  # 5 weekdays and 1 weekend day with 3 hours
    total_swimming_hours = weekly_swimming_hours * 4  # 4 weeks
    result = total_swimming_hours
    return result

print(solution())