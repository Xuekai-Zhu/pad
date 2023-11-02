def solution():
    """Bret and a team of 3 co-workers were working late so he ordered dinner for everyone. They decided on Chinese. Each main meal costs $12.0. They also ordered 2 appetizers that were $6.00 each. He includes a 20% tip and an extra $5.00 to make it a rush order. How much does Bret spend on dinner?"""
    num_meals = 4
    meal_cost = 12
    num_apps = 2
    app_cost = 6
    tip_percent = 0.2
    rush_fee = 5
    
    subtotal = (num_meals * meal_cost) + (num_apps * app_cost)
    tip = subtotal * tip_percent
    total_cost = subtotal + tip + rush_fee
    
    result = total_cost
    return result

print(solution())