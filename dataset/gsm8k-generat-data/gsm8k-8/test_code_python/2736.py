def solution():
    # Define the variables
    stories = 5
    trips_per_day = 3
    days_per_week = 7
    feet_per_story = 10

    # Calculate the total distance traveled
    total_distance = stories * trips_per_day * days_per_week * feet_per_story
    result = total_distance
    return result

print(solution())