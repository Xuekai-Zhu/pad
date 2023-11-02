def solution():
    # Calculate total hours of butterfly stroke per week
    butterfly_per_week = 3 * 4

    # Calculate total hours of backstroke per week
    backstroke_per_week = 2 * 6

    # Calculate total hours of swimming per week
    total_per_week = butterfly_per_week + backstroke_per_week

    # Calculate total hours of swimming per month (4 weeks)
    total_per_month = total_per_week * 4

    result = total_per_month
    return result

print(solution())