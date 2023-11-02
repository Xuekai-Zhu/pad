def solution():
    """Tim used to run 3 times a week but decided to add an extra 2 days a week. She runs 1 hour in the morning and 1 in the evening every day she runs. How many hours a week does she run now?"""
    original_num_days = 3
    extra_num_days = 2
    total_num_days = original_num_days + extra_num_days
    hours_per_day = 2
    total_hours_per_week = total_num_days * hours_per_day
    result = total_hours_per_week
    return result

print(solution())