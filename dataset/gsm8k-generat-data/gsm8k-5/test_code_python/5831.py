def solution():
    days_per_week = 5  # Herman buys breakfast 5 days every week
    meals_per_day = 4  # Each meal serves 4 people (Herman and 3 team members)
    cost_per_meal = 4  # Each meal costs $4.00
    weeks = 16  # The project will last for 16 weeks

    # Calculate the total cost of breakfast for the entire project
    total_cost = days_per_week * meals_per_day * cost_per_meal * weeks
    result = total_cost
    return result

print(solution())