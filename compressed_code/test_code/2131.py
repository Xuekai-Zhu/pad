def solution():
    
    stories = 5
    trips_per_day = 3
    days_per_week = 7
    feet_per_story = 10
    total_feet = 2 * (stories * feet_per_story) * trips_per_day * days_per_week
    result = total_feet
    return result

print(solution())