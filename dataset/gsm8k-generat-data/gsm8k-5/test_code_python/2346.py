def solution():
    # Calculate the amount of money John received for his old system
    old_system_value = 250
    trade_in_value = old_system_value * 0.8

    # Calculate the cost of the new system after the discount
    new_system_cost = 600 * 0.75

    # Calculate the total amount of money John spent
    total_spent = new_system_cost - trade_in_value
    result = total_spent
    return result

print(solution())