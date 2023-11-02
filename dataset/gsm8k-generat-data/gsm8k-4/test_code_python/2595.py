def solution():
    """Xavier plays football with his friends. During 15 minutes Xavier can score 2 goals on average. How many goals on average
    is Xavier able to score, when the match lasted for 2 hours?"""
    # Define the time in minutes and the average goals scored in 15 minutes
    time = 2 * 60
    goals_per_15min = 2

    # Calculate the total average goals scored during the match
    total_goals = (time / 15) * goals_per_15min

    # Calculate the average goals scored per hour
    avg_goals_per_hour = total_goals * 4

    result = avg_goals_per_hour
    return result

print(solution())