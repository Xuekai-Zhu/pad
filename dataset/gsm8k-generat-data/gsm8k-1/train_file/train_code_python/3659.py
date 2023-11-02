def solution():
    """Marco owns an ice cream truck. His ice cream cones are $5 each. If his expenses are 80% of total sales for the day, how many ice cream cones would he need to sell to make a $200 profit for the day?"""
    price_per_cone = 5
    target_profit = 200
    expenses_percent = 80
    expenses_multiplier = expenses_percent / 100
    total_expenses = target_profit / (1 - expenses_multiplier)
    cones_needed = total_expenses / price_per_cone
    result = cones_needed
    return result

print(solution())