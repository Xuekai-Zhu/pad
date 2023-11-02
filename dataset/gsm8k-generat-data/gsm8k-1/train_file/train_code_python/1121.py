def solution():
    """Tim used to run 3 times a week but decided to add an extra 2 days a week. She runs 1 hour in the morning and 1 in the evening every day she runs. How many hours a week does she run now?"""
    original_days = 3
    extra_days = 2
    morning_hours = 1
    evening_hours = 1
    total_days = original_days + extra_days
    total_hours_per_day = morning_hours + evening_hours
    total_hours = total_days * total_hours_per_day
    result = total_hours
    return result

print(solution())