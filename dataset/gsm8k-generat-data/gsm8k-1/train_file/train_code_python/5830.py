def solution():
    """When Herman’s team is busy working on large projects he stops at the drive-through 5 days, every week to buy a breakfast combo for himself and 3 members of his team. Each meal costs $4.00. This current project will last 16 weeks. How much will Herman spend on breakfast?"""
    days_per_week = 5
    team_members = 3
    meal_cost = 4
    project_length = 16
    total_meals = days_per_week * team_members * project_length
    total_cost = total_meals * meal_cost
    result = total_cost
    return result

print(solution())