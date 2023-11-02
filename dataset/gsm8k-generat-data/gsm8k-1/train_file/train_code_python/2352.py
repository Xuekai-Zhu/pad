def solution():
    """Bret and a team of 3 co-workers were working late so he ordered dinner for everyone. They decided on Chinese. Each main meal costs $12.0. They also ordered 2 appetizers that were $6.00 each. He includes a 20% tip and an extra $5.00 to make it a rush order. How much does Bret spend on dinner?"""
    num_people = 4
    cost_main_meal = 12
    num_appetizers = 2
    cost_appetizer = 6
    tip_percent = 20
    rush_order_cost = 5
    
    subtotal = (num_people * cost_main_meal) + (num_appetizers * cost_appetizer) + rush_order_cost
    tip_amount = subtotal * (tip_percent / 100)
    total_cost = subtotal + tip_amount
    
    result = total_cost
    return result

print(solution())