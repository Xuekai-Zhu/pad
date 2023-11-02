def solution():
    weekly_goal = 24  # Macy's goal is to run 24 miles per week
    daily_distance = 3  # Macy runs 3 miles per day
    days_elapsed = 6  # Macy has already run for 6 days

    # Calculate the total distance Macy has run in the past 6 days
    total_distance_run = daily_distance * days_elapsed

    # Calculate the distance Macy has left to run to meet her weekly goal
    distance_left = weekly_goal - total_distance_run
    result = distance_left
    return result

print(solution())