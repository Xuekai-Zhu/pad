def solution():
    """When Herman’s team is busy working on large projects he stops at the drive-through 5 days, every week to buy a breakfast combo for himself and 3 members of his team. Each meal costs $4.00. This current project will last 16 weeks. How much will Herman spend on breakfast?"""
    days_per_week = 5
    team_size = 3
    cost_per_meal = 4.00
    weeks = 16
    total_meals = days_per_week * team_size * weeks
    total_cost = total_meals * cost_per_meal
    result = total_cost
    return result

print(solution())