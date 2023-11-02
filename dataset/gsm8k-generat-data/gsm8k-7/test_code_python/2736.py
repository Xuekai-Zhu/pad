def solution():
    num_trips_per_day = 6 # 3 out and 3 back
    num_stories = 5
    story_height = 10
    num_days = 7

    # Calculate the total vertical distance traveled in one trip
    trip_distance = num_stories * story_height

    # Calculate the total vertical distance traveled in one day
    daily_distance = trip_distance * num_trips_per_day

    # Calculate the total vertical distance traveled in one week
    weekly_distance = daily_distance * num_days
    result = weekly_distance
    return result

print(solution())