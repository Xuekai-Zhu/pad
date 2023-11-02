def solution():
    """William's class set a goal each week of the number of cans of food that is to be collected. On the first day, 20 cans were collected. Then the number of cans increased by 5 each day. If they collected 5 days a week to reach their goal, how many cans of food was their goal per week?"""
    first_day_collection = 20
    daily_increase = 5
    days_collected = 5
    goal_per_week = first_day_collection + (daily_increase * (days_collected - 1))
    result = goal_per_week
    return result

print(solution())