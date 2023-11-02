def solution():
    """Each week Jaime saves $50. Every two weeks she spends $46 of her savings on a nice lunch with her mum. How long will it take her to save $135?"""
    weekly_savings = 50
    savings_spent_on_lunch = 46
    savings_goal = 135
    weeks_to_reach_goal = ((savings_goal - savings_spent_on_lunch) / weekly_savings) / 2
    result = weeks_to_reach_goal
    return result

print(solution())