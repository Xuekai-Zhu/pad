def solution():
    """Xavier plays football with his friends. During 15 minutes Xavier can score 2 goals on average. How many goals on average is Xavier able to score, when the match lasted for 2 hours?"""
    goals_per_15_minutes = 2
    minutes_in_2_hours = 120
    goals_per_hour = (goals_per_15_minutes*4)*60
    total_goals = goals_per_hour*2
    result = total_goals
    return result

print(solution())