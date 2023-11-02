def solution():
    """Five times a week, Onur bikes 250 kilometers a day. His friend Hanil bikes 40 more kilometers of Onur biking distance in a day. What's the total distance the two friends bikes in a week?"""
    onur_distance = 250
    hanil_distance = onur_distance + 40
    total_distance_per_day = onur_distance + hanil_distance
    total_distance_per_week = total_distance_per_day * 5
    result = total_distance_per_week
    return result

print(solution())