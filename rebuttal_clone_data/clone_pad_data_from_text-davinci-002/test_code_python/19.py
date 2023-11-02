def solution():
    """Tim rides his bike back and forth to work for each of his 5 workdays. His work is 20 miles away. He also goes for a weekend bike ride of 200 miles. If he can bike at 25 mph how much time does he spend biking a week?"""
    commute_distance = 40
    commute_time = commute_distance / 25
    commute_times_per_week = 5
    weekend_ride_distance = 200
    weekend_ride_time = weekend_ride_distance / 25
    total_time = (commute_times_per_week * commute_time) + weekend_ride_time
    result = total_time
    return result

print(solution())