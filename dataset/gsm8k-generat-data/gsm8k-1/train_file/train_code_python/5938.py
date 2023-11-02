def solution():
    """William's class set a goal each week of the number of cans of food that is to be collected. On the first day, 20 cans were collected. Then the number of cans increased by 5 each day. If they collected 5 days a week to reach their goal, how many cans of food was their goal per week?"""
    first_day_cans = 20
    cans_increase_per_day = 5
    days_per_week = 5
    total_cans_goal = first_day_cans + (cans_increase_per_day * (days_per_week-1))
    result = total_cans_goal
    return result

print(solution())