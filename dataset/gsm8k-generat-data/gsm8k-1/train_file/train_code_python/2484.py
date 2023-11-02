def solution():
    """Carly practices her butterfly stroke for 3 hours a day, 4 days a week, and her backstroke for 2 hours a day, six days a week. How much time does she spend practicing swimming in a month with 4 weeks?"""
    butterfly_hours_per_week = 3 * 4
    backstroke_hours_per_week = 2 * 6
    total_hours_per_week = butterfly_hours_per_week + backstroke_hours_per_week
    total_hours_per_month = total_hours_per_week * 4
    result = total_hours_per_month
    return result

print(solution())