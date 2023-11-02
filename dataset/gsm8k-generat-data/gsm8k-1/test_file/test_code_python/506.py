def solution():
    """For a New Year's resolution, Andy wants to lose 30 lbs. by his birthday, which is July 19th. Today is December 31st. If Andy needs to burn 3500 calories to lose a pound, how much of a calorie deficit (net amount of calories burned vs. calories consumed) does he need each day to reach his goal?"""
    goal_weight_loss = 30  # in lbs
    days_to_lose_weight = (31 + 31 + 30 + 31 + 31 + 19)  # number of days between December 31st and July 19th
    calorie_deficit_per_day = (goal_weight_loss * 3500) / days_to_lose_weight
    result = calorie_deficit_per_day
    return result

print(solution())