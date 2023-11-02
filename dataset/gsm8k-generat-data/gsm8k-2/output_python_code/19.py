def solution():
    """Tim rides his bike back and forth to work for each of his 5 workdays. His work is 20 miles away. He also goes for a weekend bike ride of 200 miles. If he can bike at 25 mph how much time does he spend biking a week?"""
    work_distance = 20 * 2 # round trip
    work_days = 5
    weekend_distance = 200
    bike_speed = 25
    total_distance = work_distance * work_days + weekend_distance
    total_time = total_distance / bike_speed
    result = total_time
    return result

print(solution())