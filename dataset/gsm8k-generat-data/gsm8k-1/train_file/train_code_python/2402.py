def solution():
    """Five times a week, Onur bikes 250 kilometers a day. His friend Hanil bikes 40 more kilometers of Onur biking distance in a day. What's the total distance the two friends bikes in a week?"""
    onur_daily_distance = 250
    hanil_daily_distance = onur_daily_distance + 40
    days_per_week = 5
    total_distance = (onur_daily_distance + hanil_daily_distance) * days_per_week
    result = total_distance
    return result

print(solution())