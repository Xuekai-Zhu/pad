def solution():
    """Xavier plays football with his friends. During 15 minutes Xavier can score 2 goals on average. How many goals on average is Xavier able to score, when the match lasted for 2 hours?"""
    goals_per_15_min = 2
    total_match_time = 2 * 60 # in minutes
    total_goals = (total_match_time / 15) * goals_per_15_min
    average_goals = total_goals / (total_match_time / 60)
    result = average_goals
    return result

print(solution())