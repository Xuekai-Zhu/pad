def solution():
    charge_per_week = 300
    pay_period = 2
    goal_amount = 1800
    weeks_to_goal = goal_amount / (charge_per_week * pay_period)
    result = weeks_to_goal
    return result

print(solution())