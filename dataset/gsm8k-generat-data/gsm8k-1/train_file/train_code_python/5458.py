def solution():
    """The bus driver drives an average of 2 hours each day, 5 days a week. From Monday to Wednesday he drove at an average speed of 12 kilometers per hour, and from Thursday to Friday at an average speed of 9 kilometers per hour. How many kilometers did the driver travel during these 5 days?"""
    days_per_week = 5
    hours_per_day = 2
    total_hours = days_per_week * hours_per_day
    distance_mon_wed = 12 * total_hours * 3
    distance_thu_fri = 9 * total_hours * 2
    total_distance = distance_mon_wed + distance_thu_fri
    result = total_distance
    return result

print(solution())