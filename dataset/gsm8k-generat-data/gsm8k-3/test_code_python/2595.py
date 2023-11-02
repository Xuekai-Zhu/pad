def solution():
    """Xavier plays football with his friends. During 15 minutes Xavier can score 2 goals on average. How many goals on average is Xavier able to score, when the match lasted for 2 hours?"""
    # Define the time of a match in minutes and the time for one goal
    MINUTES_PER_HOUR = 60
    time_of_match = 2 * MINUTES_PER_HOUR
    time_for_one_goal = 15

    # Calculate the number of goals Xavier can score during one minute
    goals_per_minute = 2 / (time_for_one_goal)

    # Calculate the number of goals Xavier can score during the whole match
    total_goals = goals_per_minute * time_of_match

    # Display the average number of goals Xavier can score during the whole match
    result = total_goals
    return result

print(solution())