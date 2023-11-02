def solution():
    num_team_members = 3
    num_days_per_week = 5
    cost_per_meal = 4.0
    num_weeks = 16

    # Calculate the total number of meals Herman will buy
    total_meals = num_team_members * num_days_per_week * num_weeks

    # Calculate the total cost of all meals
    total_cost = total_meals * cost_per_meal
    result = total_cost
    return result

print(solution())