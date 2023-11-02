def solution():
    """Jackson works 5 days a week going door-to-door collecting for charity. His goal is to raise $1000 for the week. He earned $300 on Monday and $40 on Tuesday. If he collects an average of $10 for every 4 houses he visits, how many houses will he have to visit on each of the remaining days of the week to meet his goal?"""
    days_left = 3
    remaining_goal = 1000 - 300 - 40
    houses_per_visit = 4
    money_per_visit = 10
    visits_per_day = remaining_goal / (days_left * money_per_visit)
    houses_per_day = visits_per_day * houses_per_visit
    result = houses_per_day
    return result

print(solution())