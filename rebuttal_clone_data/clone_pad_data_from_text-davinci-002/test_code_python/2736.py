def solution():
    number_of_stories = 5
    feet_per_story = 10
    trips_per_day = 3
    days_per_week = 7
    feet_traveled_per_trip = number_of_stories * feet_per_story
    total_feet_traveled = feet_traveled_per_trip * trips_per_day * days_per_week
    result = total_feet_traveled
    return result

print(solution())