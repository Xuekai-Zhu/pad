def solution():
    """Tim rides his bike back and forth to work for each of his 5 workdays. His work is 20 miles away. He also goes for a weekend bike ride of 200 miles. If he can bike at 25 mph how much time does he spend biking a week?"""
    work_days_per_week = 5
    work_distance = 20
    weekend_ride_distance = 200
    speed = 25
    time_work = (2 * work_distance * work_days_per_week) / speed
    time_weekend = weekend_ride_distance / speed
    total_time = time_work + time_weekend
    result = total_time
    return result

print(solution())