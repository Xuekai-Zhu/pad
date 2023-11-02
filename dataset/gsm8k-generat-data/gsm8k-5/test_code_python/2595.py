def solution():
    time_in_minutes = 120  # The match lasted for 2 hours, which is 120 minutes
    goals_per_15_minutes = 2  # Xavier can score 2 goals on average during 15 minutes

    # Calculate the total number of 15-minute intervals in 2 hours
    intervals = time_in_minutes / 15

    # Calculate the average number of goals Xavier can score in 2 hours
    total_goals = intervals * goals_per_15_minutes
    average_goals = total_goals / (time_in_minutes / 60)

    result = average_goals
    return result

print(solution())